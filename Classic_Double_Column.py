# https://www.overleaf.com/latex/templates/two-column-cv-template-with-moderncv/mqycjnmnswzz

def changedetails(information):
    fullname = information['fullname']
    socials = information['socials']
    objective = information['objective']
    education = information['education']
    projects = information['projects']
    publications = information['publications']
    skills = information['skills']
    languages = information['languages']
    achievements = information['achievements']
    coursework = information['course_work']
    additionals = information['additionals']
    work_experience = information['work_experiences']
    certifications = information['certifications']
    hobbies = information['hobbies']

    latex_setup = r"""
        %%%%%%%%%%%%%%%%%
        % This is a two-column CV template based on moderncv.cls
        % (v1.0, May 16 2024) written by Genki Ogaki (rockstarogk@gmail.com). Compiles with XeLaTeX.
        %
        %% It may be distributed and/or modified under the
        %% conditions of the LaTeX Project Public License, either version 1.3
        %% of this license or (at your option) any later version.
        %% The latest version of this license is in
        %%    http://www.latex-project.org/lppl.txt
        %% and version 1.3 or later is part of all distributions of LaTeX
        %% version 2003/12/01 or later.
        %%%%%%%%%%%%%%%%

        % environment
        \documentclass[11pt,a4paper]{moderncv}
        \moderncvtheme[blue]{banking}
        \nopagenumbers{}

        \usepackage[T1]{fontenc}
        \usepackage{inputenc}
        \usepackage[scale=0.9]{geometry}
        \usepackage{tabularx}
        \usepackage{mathpazo}
        \usepackage{enumitem}
        \usepackage{hyperref}


        % macro
        \renewcommand*{\labelitemi}{-}

        \newcolumntype{L}{>{\raggedright\arraybackslash}X}
        \newcolumntype{C}{>{\centering\arraybackslash}X}
        \newcolumntype{R}{>{\raggedleft\arraybackslash}X}

        \newcommand*{\experienceentry}[5][1.5mm]{
            \subsection{#2} \vspace{-1.5mm}
            \begin{tabularx}{\textwidth}{LR}
                {\itshape #3} & {\itshape #4, #5}
            \end{tabularx}
            \par\addvspace{#1}
        }

        \newcommand*{\educationentry}[4][0.5mm]{
            \begin{tabularx}{\textwidth}{LR}
                {\bfseries #3} & {\bfseries #4} \\
            \end{tabularx}
            {\itshape #2}
            \par\addvspace{#1}
        }

        \newcommand*{\scoreentry}[3][2.5mm]{
            {\bfseries #2} \\
            {\itshape #3}
            \par\addvspace{#1}
        }

        % preamble
        \firstname{""" + fullname + r"""}

        % document
        \begin{document}
        \maketitle
        \vspace{-9.0mm}

        \centering
        \begin{tabu}
            \faEnvelope\enspace \emaillink{""" + socials['mail'] + r"""} &
            \faMobile\enspace """ + socials['contact'] + r""" &
            \faLinkedin\enspace \href{""" + socials['linkedin'] + r"""}{LinkedIn} &
            \faGithub\enspace \href{""" + socials['github'] + r"""}{Github}"""
    
    try:
        if socials['website'] :
            latex_setup += r"""&
                    \faGlobe\enspace \href{""" + socials['website'] + r"""}{Website}"""
    except Exception as e:
        latex_setup += ""
        
    latex_setup += r"""\\
        \end{tabu}
        \\
        """
    
    # --------------------- PROJECTS ----------------------

    projects_latex = r"""
        % left column
        \begin{minipage}[t]{0.62\textwidth}
        \section{PROJECTS}
        \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]
        """

    project_entries = ""
    for project in projects:
        project_entries += r"""
            \item \textbf{""" + project['project_title'] + r"""}
            \hfill
            \textbf{""" + project['tech'] + r"""}\\
            """ + project['desc'] + "\n"
    
    projects_latex += (project_entries.strip() + r"\end{itemize}" + "\n")


    # --------------------- EDUCATION ----------------------

    education_latex = r"""
        \noindent

        \section{EDUCATION}
        \begin{center}
        \begin{tabularx}{\textwidth}{|m{1.5cm}|X|m{1.5cm}|m{2cm}|}
        \hline
        \hspace{0.1cm}\textbf{Course} & \hspace{0.1cm}\textbf{College / University} & \hspace{0.1cm}\textbf{Year} & \hspace{0.1cm}\textbf{Grade} \\
        \hline
        """

    education_entries = ""
    for edu in education:
        education_entries += r"""
        \hspace{0.1cm}""" + edu['qualification'] + r""" & \hspace{0.1cm}""" + edu['institution'] + r""" & \hspace{0.1cm}""" + edu['time'] + r""" & \hspace{0.1cm}""" + edu['grade'] + r""" \\
        """
    education_latex += (education_entries.strip() + "\n" +
                        r"""\hline
                            \end{tabularx}
                            \end{center}""" + "\n")
    

    # --------------------- WORK EXPERIENCES ----------------------

    work_experience_latex = ""

    if len(work_experience) :
        work_experience_latex = r"""
            \section{WORK EXPERIENCES}
            \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]
            """
        
        work_experience_entries = ""
        for work_exp in work_experience:
            work_experience_entries += r"""
                \item """ + work_exp + "\n"
        work_experience_latex += (work_experience_entries.strip() + r"""\end{itemize}""" + "\n")


    # --------------------- PUBLICATIONS ----------------------

    publications_latex = ""

    if len(publications) != 0:
        publications_latex = r"""
            \section{PUBLICATIONS}
            \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]
            """

        publications_entries = ""
        for pub in publications:
            publications_entries += r"""
                \item """ + pub + "\n"
        publications_latex += (publications_entries.strip() + r"\end{itemize}" + "\n")


    # --------------------- ADDITIONAL ENGAGEMENTS ----------------------

    additionals_latex = ""

    if len(additionals) != 0:
        additionals_latex = r"""
            \section{ADDITIONAL ENGAGEMENTS}
            \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]
            """
        
        for additional in additionals :
            additionals_latex += r"""\item """ + additional + "\n"

        additionals_latex += r"\end{itemize}"


    # --------------------- COURSE WORK ----------------------

    coursework_latex = r"""
        \section{COURSE WORK}
        \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]
        """

    coursework_entries = ""

    for course in coursework.split(",") :
        coursework_entries += r"""\item """ + course + "\n"

    coursework_latex += coursework_entries + r"""
        \end{itemize}

        \end{minipage}
        \hfill"""


    # --------------------- SUMMARY / OBJECTIVE ----------------------

    summary_latex = r"""
        % right column
        \begin{minipage}[t]{0.35\textwidth}
        \section{SUMMARY}
        """

    summary_latex += r"""
        """ + objective + "\n"
    
    # --------------------- SKILLS ----------------------

    skills_latex = r"""
        \section{SKILLS}
        \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]
        """
    
    skills_entries = ""
    for skill in skills:
        skills_entries += r"""
            \item """ + skill + "\n"
    skills_latex += (skills_entries.strip() +  r"\end{itemize}" + "\n")


    # --------------------- LANGUAGES ----------------------

    languages_latex = r"""
        \section{LANGUAGES}
        """

    languages_entries = ""
    for language in languages:
        if languages.index(language) == len(languages) - 1 :
            languages_entries += language
        else:
            languages_entries += language + r""", """

    languages_latex += languages_entries


    # --------------------- HOBBIES ----------------------

    hobbies_latex = r"""
        \section{HOBBIES}
        """

    hobbies_latex += hobbies


    # --------------------- CERTIFICATIONS ----------------------

    certifications_latex = ""

    if len(certifications) != 0:
        certifications_latex = r"""
            \section{CERTIFICATIONS}
            \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]
            """

        certifications_entries = ""
        for cert in certifications:
            certifications_entries += r"""
                \item """ + cert + "\n"
        certifications_latex += (certifications_entries.strip() +  r"\end{itemize}" + "\n")


    # --------------------- ACHIEVEMENTS ----------------------

    achievements_latex = ""

    if len(achievements) != 0 :
        achievements_latex = r"""
            \section{ACHIEVEMENTS}
            \begin{itemize}[label=\textbullet, itemsep=1pt, topsep=0pt]"""
        
        achievements_entries = ""
        for achieve in achievements:
            achievements_entries += r"""
                \item """ + achieve + "\n"
        achievements_latex += (achievements_entries.strip() + r"""\end{itemize}""")

    close_latex = r"""\end{minipage}
            \end{document}"""

    # --------------------- PUTTING THEM ALL TOGETHER ----------------------

    latex_document = (latex_setup + 
                      projects_latex + education_latex + 
                      work_experience_latex + publications_latex + 
                      additionals_latex + coursework_latex + 
                      summary_latex + skills_latex + languages_latex + 
                      hobbies_latex + certifications_latex + achievements_latex + close_latex)

    return latex_document

"""information = {
    'fullname' : 'Venu Pulagam',
    'socials' : {
        'github': 'https://github.com/venupulagam',
        'linkedin': 'https://linkedin.com/in/venupulagam',
        'mail': 'venupulagam@example.com',
        'contact': '+91-9999999999',
        'website': 'https://venupulagam.com'
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
    'publications': [],
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
