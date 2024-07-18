# https://www.overleaf.com/latex/templates/nsut-tnp-resume/sxzbtkwmqsyg

def changedetails(information):
    fullname = information['fullname'] #done
    socials = information['socials'] #done
    objective = information['objective'] #done
    education = information['education'] #done
    projects = information['projects'] #done
    publications = information['publications'] #done
    skills = information['skills'] #done
    languages = information['languages'] #done
    achievements = information['achievements'] #done
    coursework = information['course_work'] #done
    additionals = information['additionals'] #done
    work_experience = information['work_experiences'] #done
    certifications = information['certifications'] #done
    hobbies = information['hobbies'] #done

    latex_setup = r"""
    \documentclass[11pt,article]{article}
    \usepackage[letterpaper,margin=0.5in]{geometry}
    \usepackage{graphicx}
    \usepackage{booktabs}
    \usepackage{url}
    \usepackage{enumitem}
    \usepackage{palatino}
    \usepackage{tabularx}
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage{color}
    \definecolor{mygrey}{gray}{0.82}
    \usepackage{hyperref}
    \hypersetup{
        hidelinks,
        colorlinks=true,
        urlcolor=blue
    }

    \setlength{\tabcolsep}{0in}
    \newcommand{\isep}{-2pt}
    \newcommand{\lsep}{-0.5cm}
    \newcommand{\psep}{-0.6cm}
    \renewcommand{\labelitemii}{$\circ$}

    \pagestyle{empty}

    \newcommand{\resitem}[1]{\item #1 \vspace{-2pt}}
    \newcommand{\resheading}[1]{{\small \colorbox{mygrey} { \begin{minipage}{0.99\textwidth}{\textbf{#1 \vphantom{p\^{E}}}}\end{minipage}}}}
    \newcommand{\ressubheading}[3]{
    \begin{tabular*}{6.62in}{l @{\extracolsep{\fill}} r}
        \textsc{{\textbf{#1}}} & \rightline\textsc{\textit{[#2]}} \\
    \end{tabular*}\vspace{-8pt}}

    \begin{document}
    \begin{table}
        \begin{minipage}{1\linewidth}
            \centering
            \def\arraystretch{1}
            \textbf{\Large{""" + fullname + r"""}}\\ \vspace{0.4em}
            """ + socials['contact'] + r""" |
            \href{mailto:""" + socials['mail'] + r"""}{Email} |
            \href{""" + socials['linkedin'] + r"""}{LinkedIn} |
            \href{""" + socials['github'] + r"""}{Github}"""
    
    try:
        if socials['website'] :
            latex_setup += r"""|
                \href{""" + socials['website'] + r"""}{Website}"""
    except Exception as e:
        latex_setup += ""
    
    latex_setup += r"""
        \end{minipage}\hfill
    \end{table}
    \setlength{\tabcolsep}{18pt}

    \noindent
    \resheading{\textbf{OBJECTIVE}}\\[-0.9pt]\\
    """ + objective + r"""
    \\
    """

    # --------------------- EDUCATION ----------------------

    education_latex = r"""
    \noindent
    \resheading{\textbf{EDUCATION}}\\[-0.9pt]\\
    \begin{tabularx}{\textwidth}{X l r l}
    \textbf{Course} & \textbf{College / University} & \textbf{Year} & \textbf{CGPA / \%} \\
    \toprule
    """

    education_entries = ""
    for edu in education:
        education_entries += r"""
        """ + edu['qualification'] + " & " + edu['institution'] + " & " + edu['time'] + " & " + edu['grade'] + r""" \\
        """

    education_entries += r"""
    \end{tabularx}
    \vspace{1pt}
    """

    education_latex += education_entries


    # --------------------- WORK EXPERIENCES ----------------------

    work_experience_latex = ""

    if len(work_experience) != 0 :
        work_experience_latex = r"""
        \noindent
        \resheading{\textbf{WORK EXPERIENCE}}\\[-0.9pt]
        \begin{itemize}[itemsep=1pt, topsep=0pt]"""

        work_experience_entries = ""
        for experience in work_experience:
            work_experience_entries += r"""\item """ + experience

        work_experience_entries += r"""
            \\
            \end{itemize}
            """
        
        work_experience_latex += work_experience_entries


    # --------------------- PROJECTS ----------------------


    projects_latex = r"""
        \noindent
        \resheading{\textbf{PROJECTS}}\\[-0.9pt]
        \begin{itemize}[itemsep=1pt, topsep=0pt]
        """

    project_entries = ""
    for proj in projects:
        project_entries += r"""
        \item \textbf{""" + proj['project_title'] + r"""}
        \hfill 
        \textbf{""" + proj['tech'] + r"""}\\
        """ + proj['desc']

    project_entries += r"""
    \\
    \end{itemize}
    """

    projects_latex += project_entries


    # --------------------- PUBLICATIONS ----------------------

    publications_latex = ""

    if len(publications) != 0:
        publications_latex = r"""
            \noindent
            \resheading{\textbf{PUBLICATIONS}}\\[-0.9pt]
            \begin{itemize}[itemsep=1pt, topsep=0pt]
            """

        publication_entries = ""
        for publication in publications:
            publication_entries += r"""\item """ + publication

        publication_entries += r"""
        \\
        \end{itemize}
        """

        publications_latex += publication_entries
    

    # --------------------- COURSE WORK ----------------------


    coursework_latex = r"""
    \noindent
    \resheading{\textbf{COURSE WORK}}\\[-0.9pt]\\
    """

    coursework_latex += coursework + r"\\" + "\n"


    # --------------------- ACHIEVEMENTS ----------------------

    achievements_latex = ""

    if len(achievements) != 0:
        achievements_latex = r"""
        \noindent
        \resheading{\textbf{ACHIEVEMENTS}}\\[-0.9pt]
        \begin{itemize}[itemsep=1pt, topsep=0pt]
        """
        achievements_entries = ""
        for achievement in achievements:
            achievements_entries += r"""
            \item """ + achievement

        achievements_entries += r"""
        \\
        \end{itemize}
        """

        achievements_latex += achievements_entries


    # --------------------- SKILLS ----------------------

    skills_latex = r"""
    \noindent
    \resheading{\textbf{SKILLS}}\\[-0.9pt]\\
    """

    skills_entries = ""
    for skill in skills:
        if skills.index(skill) == len(skills)-1 :
            skills_entries += skill
        else :
            skills_entries += skill + r""", """

    skills_latex += (skills_entries +  r"\\" + "\n")


    # --------------------- LANGUAGES ----------------------

    languages_latex = r"""
    \noindent
    \resheading{\textbf{LANGUAGES}}\\[-0.9pt]\\
    """

    languages_entries = ""
    for language in languages:
        if languages.index(language) == len(languages) - 1 :
            languages_entries += language
        else:
            languages_entries += language + r""", """

    languages_latex += (languages_entries +  r"\\" + "\n")
                        

    # --------------------- ADDITIONAL ENGAGEMENTS ----------------------

    additionals_latex = ""

    if len(additionals) != 0:
        additionals_latex = r"""
        \noindent
        \resheading{\textbf{ADDITIONAL ENGAGEMENTS / NON-TECHNICAL ACTIVITIES}}\\[-0.9pt]
        \begin{itemize}[itemsep=1pt, topsep=0pt]
        """

        additionals_entries = ""
        for additional in additionals:
            additionals_entries += r"""\item """ + additional

        additionals_latex += (additionals_entries + r"""
        \\
        \end{itemize}""")


    # --------------------- CERTIFICATIONS ----------------------

    certifications_latex = ""

    if len(certifications) != 0:
        certifications_latex = r"""
        \noindent
        \resheading{\textbf{CERTIFICATIONS}}\\[-0.9pt]
        \begin{itemize}[itemsep=1pt, topsep=0pt]
        """

        certifications_entries = ""
        for certification in certifications:
            certifications_entries += r"""\item """ + certification

        certifications_latex += (certifications_entries + r"""\\
        \end{itemize}""")


    # --------------------- HOBBIES AND INTERESTS ----------------------

    hobbies_latex = r"""
    \noindent
    \resheading{\textbf{HOBBIES AND INTERESTS}}\\[-0.9pt]\\
    """ + hobbies + r"""
    \\
    \end{document}
    """

    # --------------------- PUTTING THEM ALL TOGETHER ----------------------

    latex_document = (latex_setup 
                    + education_latex
                    + work_experience_latex
                    + projects_latex 
                    + publications_latex 
                    + coursework_latex 
                    + achievements_latex 
                    + skills_latex 
                    + languages_latex 
                    + additionals_latex 
                    + certifications_latex 
                    + hobbies_latex)
    
    return latex_document

"""information = {
    'fullname' : 'Venu Pulagam',
    'socials' : {
        'github': 'https://github.com/venupulagam',
        'linkedin': 'https://linkedin.com/in/venupulagam',
        'mail': 'venupulagam@example.com',
        'contact': '+91-9999999999',
        'website': 'www.google.com'
    },
    'objective' : "Objective statement here.",
    'education' : [
        {'institution': 'University', 'qualification': 'Degree', 'grade': 'GPA', 'time': '1990'},
        {'institution': 'High School', 'qualification': '12', 'grade': '990', 'time': '1989'},
        {'institution': 'School', 'qualification': '10', 'grade': '10', 'time': '1987'}
    ],
    'projects' : [
        {'project_title': 'HiSt', 'desc': 'Description', 'tech': 'Python, Java'},
        {'project_title': 'Gogle', 'desc': 'Description for Gogle', 'tech': 'Python, Java'}
    ],
    'publications': ['Published this paper', 'Published that Paper'],
    'skills' : ['Skill 1', 'Skill 2', 'Skill 3'],
    'languages': ['Python', 'Java', 'HTML', 'CSS'],
    'achievements': ['Achieved this thing, 2019', 'Achieved that thing, 2020'],
    'course_work': 'Machine Learning, Transfer Learning',
    'additionals': ['Acted in a short film', 'Directed a short film'],
    'work_experiences': ['Worked as this', 'Worked as that'],
    'certifications': ['Certificate 1', 'Certificate 2'],
    'hobbies' : 'Dancing, Singing.'
}

resume = changedetails(information)
print(resume)"""
