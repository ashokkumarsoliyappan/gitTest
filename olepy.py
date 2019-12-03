import docx
import os

data = ['test.png','test1.png']
i = 0
doc = docx.Document("testing.docx")
for oleEmbed in doc.inline_shapes :
	picture_ns = nsmap['pic']
	blip_bldr = a_blip()
	if embed:
		blip_bldr.with_embed('rId1')
		if link:
			blip_bldr.with_link('rId2')
			inline = (an_inline().with_nsdecls('wp', 'r').with_child(a_graphic().with_nsdecls().with_child(a_graphicData().with_uri(picture_ns).with_child(a_pic().with_nsdecls().with_child(a_blipFill().with_child(blip_bldr)))))).element
			fr = open(data[i], "wb")
			fr.write(inline._blob)
	i += 1
fr.close()