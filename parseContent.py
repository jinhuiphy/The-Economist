import re

# 处理原始目录，

input = "rawContent.txt"
output = "genContent.txt"
final = "finalContent.txt"

titleList = ["The world this week", "Leaders", "Letters", "Briefing", "United States", "The Americas", "Asia", "China", "Middle East & Africa", "Europe", "Britain", "International", "Business", "Science & technology", "Books & arts", "Economic & financial indicators", "Graphic detail", "Obituary"]

genContent = []

outfile = open(output, "w", encoding="UTF8")
# outfile.write("Cover    1\nContents 5\n")
with open(input, "r", encoding="UTF8") as rawContent:
    newLine = ""
    flag = False
    for cnt, line in enumerate(rawContent):
        line = line.rstrip()
        if line in titleList:
            if cnt == 0:
                outfile.write(line)
            else:
                outfile.write("\n" + line)
            flag = True
        elif line[0].isdigit():
            try:
                result = re.match("(^[0-9]+) (.*)$", line)
                page = (result.group(1))
            except AttributeError as identifier:
                print("Error in line: " + line)
                break
            if flag:
                outfile.write("\t{}\n{}".format(page, line))
                flag = False
            else:
                outfile.write("\n{}".format(line))
        else:
            outfile.write(" " + line)
outfile.close()

finalfile = open(final, "w", encoding="UTF8")
finalfile.write("Cover\t1\nContents\t3\n")
with open(output, "r", encoding="UTF8") as fp:
    for cnt, line in enumerate(fp):
        if line[0].isdigit():
            res = re.match("(^[0-9]+) (.*)", line)
            line = ("\t{}\t{}\n".format(res.group(2), res.group(1)))
        finalfile.write(line)
finalfile.close()