import docx
 
def ReadingTextDocuments(filename):
    doc = docx.Document(filename)

    completed = []

    for p in doc.paragraphs:
        completed.append(p.text)

    return '\n'.join(completed)

print(ReadingTextDocuments("read1.docx"))