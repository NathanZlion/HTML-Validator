
from stack import Stack

class checkHtml:
    
    def htmlValidator(self, file):
        myStack = Stack()
        empty_element=["img", "br", "hr", ]   #this is not full yet add more empty elements for a more reliable output
        theFile = open(file,'r', encoding = "utf8")
        fileContent = theFile.read()
        theFile.close()
        index = 0

        if fileContent[:15].lower() == '<!doctype html>' or fileContent[:15].lower() == '<!DOCTYPE html>':
            index = 15
        history = "\n"
        while index < (len(fileContent)):
            if fileContent[index] == "<":
                openingTag = ""
                index += 1

                # It's an opening tag.
                if fileContent[index] != "/":
                    while fileContent[index] != '>' and fileContent[index] != " ":
                        openingTag += fileContent[index]
                        index += 1

                    if openingTag[-1] == "/":
                        pass
                    elif openingTag not in empty_element:    
                        myStack.push(openingTag)
                        history += ("\n" + str(myStack))

                    while fileContent[index] != ">":
                        index += 1

                if fileContent[index] == "/":
                    closingtag = ""
                    index += 1
                    while fileContent[index] != ">":
                        closingtag += fileContent[index]
                        index += 1
                    
                    if not myStack.isEmpty():
                        if (myStack.peek() == closingtag):
                            myStack.pop()
                            history += ("\n" + str(myStack))
                        elif (closingtag in empty_element):
                            pass
                        else:
                            data=open(file).read()[: index + 1]
                            error_line=len(data.split('\n'))
                            history += ("\n" + str(myStack))
                            return "⁞ Error found at line " +str(error_line)+ " :  </"+closingtag +"> ; ⁞ \n⁞<" + myStack.pop() + "> should have been closed first.⁞ "
            index += 1

        if myStack.isEmpty():
            return  " ⁞ √ Valid Html, congra :) ⁞", history
        
        return "Invalid Html →  ⁞ <" + myStack.pop() + "> tag is not closed  ⁞", history
    
    def validate(self, file):
        result, history = self.htmlValidator(file)
        return result

    def history(self, file):
        result, history = self.htmlValidator(file)
        return history
    
    def showfile(self, file):
        filee = open(file, 'r', encoding="utf8")
        filecontent = filee.read()
        filee.close()

        print("\n\n\t\t<!--The file you requested is displayed below.-->\n\n" + "~"*100)
        print(filecontent)
        print("~"*100)
HTML = checkHtml()

# print(HTML.history('file.html'))
# HTML.showfile('file.html')
# print(HTML.validate('file.html'))
