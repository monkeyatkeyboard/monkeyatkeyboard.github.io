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
    
    # print("Extracting")
    text = Extract(pdf)

    # print("Summarizing:")
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
def Get_Text_Summary(text):
    import os

    from pdf_extraction import Extract  # Referencing as Extract for now
    from summarize import Summarize  # Referencing as Summarize for now
    
    # print("Summarizing:")
    stripped_text = text.replace("\n", "")
    summary = Summarize(text, 0.2) 
    
    i = 0
    while i < len(summary):
        try:
            if summary[i] in [".", "?", "!"] and (summary[i+1] == " " or summary[i+1].isupper()):
                # Line break and bullet point for important sentences
                summary = summary[:i+1] + "<br>- " + summary[i+1:]
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
    summary = Get_Text_Summary("""The Exploration of Space

Humanity's fascination with the cosmos has driven us to explore the vast expanse of space for centuries. From ancient astronomers peering into the night sky to modern space agencies launching missions to distant planets and beyond, the quest to understand the universe continues to captivate our imagination. The pioneering efforts of scientists, engineers, and astronauts have led to groundbreaking discoveries, such as the identification of exoplanets, the study of cosmic phenomena like black holes and neutron stars, and the search for signs of extraterrestrial life.

Environmental Conservation

In recent years, the importance of environmental conservation has gained significant momentum. Climate change, habitat destruction, and biodiversity loss have all raised concerns about the long-term sustainability of our planet. Efforts to combat these issues include international agreements like the Paris Agreement, which aims to reduce greenhouse gas emissions, as well as grassroots movements advocating for sustainable practices, wildlife conservation, and reforestation. The preservation of Earth's ecosystems and the promotion of eco-friendly technologies are critical components of this global effort.

The Evolution of Technology

The rapid advancement of technology has transformed nearly every aspect of human life. From the invention of the wheel and the printing press to the digital age of smartphones and artificial intelligence, innovation continues to shape our world. The development of the internet and the proliferation of social media have reshaped communication and social interactions, while breakthroughs in fields like medicine, robotics, and renewable energy have the potential to revolutionize our future. The ethical and societal implications of these technological advancements are ongoing topics of debate and concern.

Cultural Diversity

The world is a tapestry of diverse cultures, languages, and traditions. Cultural diversity is both a source of enrichment and a challenge, as societies grapple with issues related to identity, inclusion, and discrimination. The celebration of cultural heritage, the promotion of intercultural understanding, and the preservation of indigenous knowledge are all crucial elements in fostering a more inclusive and equitable global community. Respect for cultural diversity is not only a matter of human rights but also a wellspring of creativity and innovation.

The Power of Education

Education is often described as the key to personal and societal progress. It empowers individuals to learn, grow, and fulfill their potential. Moreover, education plays a vital role in economic development, as an educated workforce is a driving force behind innovation and productivity. Access to quality education, however, remains a challenge in many parts of the world. Efforts to promote inclusive and equitable education for all, regardless of gender, socioeconomic status, or geographic location, are crucial for building a brighter future.

The Challenges of Healthcare

The healthcare industry faces a range of complex challenges. Access to quality healthcare, the rising costs of medical treatment, and the global response to health crises, such as the COVID-19 pandemic, are all significant issues. Medical research and technology advancements, such as gene editing and telemedicine, offer hope for improving healthcare delivery and treatment outcomes. However, ethical dilemmas and questions about the equitable distribution of healthcare resources continue to shape the debate around the future of medicine.

The Beauty of Art and Culture

Art and culture are expressions of the human spirit, reflecting the richness of our experiences and our creativity. Whether in the form of visual arts, music, literature, dance, or theater, they provide avenues for self-expression and connection with others. Museums, galleries, theaters, and cultural festivals celebrate the diverse expressions of art, offering opportunities for cultural enrichment and creative exploration. Art has the power to challenge societal norms, provoke thought, and bring people together in shared appreciation of beauty and meaning.

The Dynamics of Politics

Political systems are the structures through which societies make decisions, allocate resources, and address their collective needs. Democracy, authoritarianism, monarchy, and other forms of governance have their strengths and weaknesses. Elections, policies, and international diplomacy all shape the course of nations. Citizens' engagement in the political process, advocacy for human rights, and the pursuit of justice are essential components of any functioning democracy. The global balance of power and the evolving role of international institutions add layers of complexity to the political landscape.

The Quest for Knowledge

Curiosity is at the core of human nature, and our pursuit of knowledge is relentless. From the scientific method to philosophical inquiries, humans have strived to understand the mysteries of the universe and the meaning of life. Research, experimentation, and critical thinking drive the quest for knowledge in fields ranging from physics and biology to psychology and sociology. The relentless pursuit of knowledge not only expands our horizons but also inspires innovation and drives the progress of human society.

This diverse range of topics highlights the multifaceted nature of our world and the ongoing human endeavor to explore, understand, and shape it.""")
    print(summary)



