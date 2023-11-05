# Turned main into function
# Needs to be a path to a PDF file
def Get_PDF_Summary(filename):
    # pip install PyPDF2
    import os

    from pdf_extraction import Extract  # Referencing as Extract for now
    from summarize import Summarize  # Referencing as Summarize for now


    pdf = filename
    abs_path = os.path.abspath(os.path.curdir)
    curr_file = abs_path + "/" + pdf
    
    print("Extracting")
    text = Extract(pdf)

    print("Summarizing:")
    summary = Summarize(text, 0.1) 

    i = 0
    while i < len(summary):
        try:
            if summary[i] in [".", "?", "!"] and (summary[i+1] == " " or summary[i+1].isupper()):
                # Line break and bullet point for important sentences
                summary = summary[:i+1] + "\n- " + summary[i+1:]
                # print(summary[i-15:i+15])
                i += 1
            
        except IndexError:
            break
        i += 1
    
    i = 0
    while i < len(summary):
        try:
            if summary[i] == " " and summary[i+1] == " ":
                summary = summary[:i] + summary[i+1:]
                # print(summary[i-15:i+15])
        except IndexError:
            break
        i += 1
    
    # Adds dash to first sentence
    summary = "- " + summary
             
    #print("Printing Summary:")
    return summary


## If no PDF, call this function
## Im going to assume this is going to be shorter?
def Get_Text_Summary:
    print("Summarizing:")
    summary = Summarize(text, 0.5) 

    i = 0
    while i < len(summary):
        try:
            if summary[i] in [".", "?", "!"] and (summary[i+1] == " " or summary[i+1].isupper()):
                # Line break and bullet point for important sentences
                summary = summary[:i+1] + "\n- " + summary[i+1:]
                # print(summary[i-15:i+15])
                i += 1
            
        except IndexError:
            break
        i += 1
    
    i = 0
    while i < len(summary):
        try:
            if summary[i] == " " and summary[i+1] == " ":
                summary = summary[:i] + summary[i+1:]
                # print(summary[i-15:i+15])
        except IndexError:
            break
        i += 1
    
    # Adds dash to first sentence
    summary = "- " + summary
             
    #print("Printing Summary:")
    return summary


# Will run an example pdf if this file is run as main
if __name__ == "__main__":
    summary = Get_PDF_Summary("BackEnd/2005 Daw et al. natneuro.pdf")
    print(summary)



