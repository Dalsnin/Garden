import re
import sqlite3
from markupsafe import Markup

def get_blogposts():
    def get_data_from_sql():
        try:
            connection = sqlite3.connect('backend/blogposts.db')
        except:          
            connection = sqlite3.connect('/home/Dalsnin/mysite/backend/blogposts.db')
        cursor = connection.cursor()   
 
        cursor.execute('''SELECT * from blogposts ORDER BY publish_priority DESC''')

        blogentries = []
        for row in cursor:
            tmpdict = {}
            tmpdict['blogpost'] = row[1]
            tmpdict['title'] = row[2]
            tmpdict['publish_date'] = row[3]
            tmpdict['shown'] = row[4]
            blogentries.append(tmpdict)

        return(blogentries)

        connection.close()


    def insert_images_markup(text):
        # {{}} designates file names.
        # {} designates picture quote
        # It should follow this format:
        #           Text from blogpost
        #           {{
        #           quoted string          
        #           }}
        #           {picturename}
        #
        text = text.replace("{{", '<div class="quote">')
        text = text.replace("}}", '</div>')
        text = text.replace("{", '<img src="static/images/')
        text = text.replace("}", '/960 x 720.jpg" alt="Smiley face" width="960" height="720">')

        # When a user writes to SQL, a new line is designated \n. In HTML however, a new line is understood as a <p>.
        text = text.replace('\n\n', '</p><p>')
        text = text.replace('\n', '<p>')
        return text


    blogentries = get_data_from_sql()
    for i in range(len(blogentries)):
        blogentries[i]['blogpost'] = insert_images_markup(blogentries[i]['blogpost'])
        blogentries[i]['blogpost'] = Markup(blogentries[i]['blogpost'])

    return(blogentries)

