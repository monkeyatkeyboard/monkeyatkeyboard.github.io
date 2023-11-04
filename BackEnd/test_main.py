
if __name__ == "__main__":
    # pip install PyPDF2
    import os

    from pdf_extraction import Extract  # Referencing as Extract for now
    from summarize import Summarize  # Referencing as Summarize for now


    # Replace with value put in later?
    pdf = "ticket.pdf"
    abs_path = os.path.abspath(os.path.curdir)
    curr_file = abs_path + "/" + pdf
    

    text = Extract(pdf)
    summary = Summarize(text) 
    print(summary)





