# Scrape steam game data and show popular new releases as a webpage

# AgGrid implement help: https://medium.com/the-streamlit-teacher/enhancing-aggrid-table-with-image-display-in-streamlit-apps-425b6e989d5b

import requests
import lxml.html
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, JsCode 
from st_aggrid.grid_options_builder import GridOptionsBuilder

st.title("""Steam Popular New Releases""")

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

tags = []
for tag in new_releases.xpath('.//div[@class="tab_item_top_tags"]'):
	tags.append(tag.text_content())

tags = [tag.split(', ') for tag in tags] 
platforms_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []

for game in platforms_div:
	temp = game.xpath('.//span[contains(@class, "platform_img")]') 
	platforms = [t.get('class').split(' ')[-1] for t in temp]
	if 'hmd_separator' in platforms:
		platforms.remove('hmd_separator')
	total_platforms.append(platforms)

images = []
for image in new_releases.xpath('.//img[@class="tab_item_cap_img"]/@src'):
    images.append(image)

output = []
for info in zip(titles, prices, tags, total_platforms, images):
    resp = {}
    resp['title'] = info[0]
    resp['price'] = info[1]
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    resp['image'] = info[4]
    output.append(resp)


#print(len(output))
#print(output)
df = pd.DataFrame(output)
st.write(df)
#table = st.table(output)

# render_image = JsCode('''
#     function renderImage(params) {
#         // Create a new image element
#         var img = new Image();

#         // Set the src property to the value of the cell (should be a URL pointing to an image)
#         var url = params.value.split("?")[0] + ".jpg";
#         img.src = url;

#         // Set the width and height of the image to 50 pixels
#         img.width = 184;
#         img.height = 69;

#         // Return the image element
#         return img;
#     }
# ''')

render_image = JsCode('''
    function renderImage(params) {
        const imgSrc = params.value;
        const imgHtml = `<img src="${imgSrc}" width="50" height="50"/>`;
        return imgHtml;
    }
''')


# Build GridOptions object
options_builder = GridOptionsBuilder.from_dataframe(df)
options_builder.configure_column('image', cellRenderer = render_image)
options_builder.configure_selection(selection_mode="single", use_checkbox=True)
grid_options = options_builder.build()

# Create AgGrid component
grid = AgGrid(df, 
                gridOptions = grid_options,
                allow_unsafe_jscode=True,
                height=200, width=500, theme='streamlit')

sel_row = grid["selected_rows"]
if sel_row:
  with st.expander("Selections", expanded=True):
    col1,col2 = st.columns(2)
    st.info(sel_row[0]['tags'])              
    col1.image(sel_row[0]['image'],caption=sel_row[0]['title'])
