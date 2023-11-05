
if __name__ == "__main__":
    # pip install PyPDF2
    import os

    from pdf_extraction import Extract  # Referencing as Extract for now
    #from summarize import Summarize  # Referencing as Summarize for now
    # Test to see as proof of concept
    from test_summarize import Summarize2


    # Replace with value put in later?
    pdf = "1. The Black Cat Author Edgar Allan Poe.pdf"
    abs_path = os.path.abspath(os.path.curdir)
    curr_file = abs_path + "/" + pdf
    

    # Take out prints and switch Summarize2 to Summarize when ready
    print("Exctracting")
    text = Extract(pdf)

    print("Summarizing:")
    summary = Summarize2(text) 

    print("Printing Summary:")
    print(summary)





