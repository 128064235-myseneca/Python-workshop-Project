from pathlib import Path
import markdown

inp=Path(input("enter the input path with file name: "))
out=Path(input("enter the output path only: "))
outFile=input("enter the output file name: ")
outTot=str(out)+"/"+outFile

if inp.exists()==True and out.exists()==True:
    markdown.markdownFromFile(str(inp),outTot)
else:
    print("path wrong")
