import pdfkit


config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")

#pdfkit.from_url(https://pdfcrowd.com/doc/api/html-to-pdf/python/, out.pdf,configuration=config)

name=input('Enter Name: ')
courseName=input('Enter Course Name: ')
score=input('Enter Score: ')


html="""<center>
<style>
.signature, .title { 
float:left;
  border-top: 1px solid #000;
  width: 200px; 
  text-align: center;
}
</style>
<div style="width:800px; height:600px; padding:20px; text-align:center; border: 10px solid #787878">
<div style="width:750px; height:550px; padding:20px; text-align:center; border: 5px solid #787878">
       <span style="font-size:50px; font-weight:bold">Certificate of Completion</span>
       <br><br>
       <span style="font-size:25px"><i>This is to certify that</i></span>
       <br><br>
       <span style="font-size:30px"><b>"""+name+"""</b></span><br/><br/>
       <span style="font-size:25px"><i>has completed the course</i></span> <br/><br/>
       <span style="font-size:30px">"""+courseName+"""</span> <br/><br/>
       <span style="font-size:20px">with score of <b>"""+score+"""</b></span> <br/><br/><br/><br/>
       <span style="font-size:25px"><i>Completed Date</i></span><br>
       <span style="font-size:25px"><i>29-Oct-2019</i></span><br>
<table style="margin-top:40px;float:left">
<tr>
<td><span><b>"""+name+"""</b></td>
</tr>
<tr>
<td style="width:200px;float:left;border:0;border-bottom:1px solid #000;"></td>
</tr>
<tr>
<td style="text-align:center"><span><b>Signature</b></td>
</tr>
</table>
<table style="margin-top:40px;float:right">
<tr>
<td><span><b>"""+name+"""</b></td>
</tr>
<tr>
<td style="width:200px;float:right;border:0;border-bottom:1px solid #000;"></td>
</tr>
<tr>
<td style="text-align:center"><span><b>Signature</b></td>
</tr>
</table>
</div>
</div>
</center>"""
pdfkit.from_string(html, 'MyPDF.pdf', configuration=config)

#pdfkit.from_file('index.html', 'out.pdf')
print('Pdf Has been sucessfully created')
