import re
a='''<table>
     <tr>
     <td>this is one
     </td>
     <td>
     this is two
     </td>
     </tr>
     <tr><td>three</td><td>four</td></tr>
     </table>'''
aaa=re.findall("<td>(.*?)</td>",a)
print(aaa)