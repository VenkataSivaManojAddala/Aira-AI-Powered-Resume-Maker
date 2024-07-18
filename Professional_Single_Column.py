# https://www.overleaf.com/latex/templates/resume-professional-template-software-engineer/ttwtyxskrcsz

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
        %-------------------------
        % Resume in Latex
        % Author : Vaishanth
        % License : MIT
        %------------------------

        \documentclass[letterpaper,11pt]{article}

        \usepackage{latexsym}
        \usepackage[empty]{fullpage}
        \usepackage{titlesec}
        \usepackage{marvosym}
        \usepackage[usenames,dvipsnames]{color}
        \usepackage{verbatim}
        \usepackage{enumitem}
        \usepackage[hidelinks]{hyperref}
        \usepackage[english]{babel}
        \usepackage{tabularx}
        \usepackage{fontawesome5}
        \usepackage{multicol}
        \usepackage{graphicx}%\setmainfont{Times New Roman}
        \setlength{\multicolsep}{-3.0pt}
        \setlength{\columnsep}{-1pt}
        \input{glyphtounicode}

        \RequirePackage{tikz}
        \RequirePackage{xcolor}

        \definecolor{cvblue}{HTML}{0E5484}
        \definecolor{black}{HTML}{130810}
        \definecolor{darkcolor}{HTML}{0F4539}
        \definecolor{cvgreen}{HTML}{3BD80D}
        \definecolor{taggreen}{HTML}{00E278}
        \definecolor{SlateGrey}{HTML}{2E2E2E}
        \definecolor{LightGrey}{HTML}{666666}
        \colorlet{name}{black}
        \colorlet{tagline}{darkcolor}
        \colorlet{heading}{darkcolor}
        \colorlet{headingrule}{cvblue}
        \colorlet{accent}{darkcolor}
        \colorlet{emphasis}{SlateGrey}
        \colorlet{body}{LightGrey}

        % serif
        \usepackage{CormorantGaramond}
        \usepackage{charter}

        % Adjust margins
        \addtolength{\oddsidemargin}{-0.6in}
        \addtolength{\evensidemargin}{-0.5in}
        \addtolength{\textwidth}{1.19in}
        \addtolength{\topmargin}{-.7in}
        \addtolength{\textheight}{1.4in}
        \urlstyle{same}

        \definecolor{airforceblue}{rgb}{0.36, 0.54, 0.66}

        \raggedbottom
        \raggedright
        \setlength{\tabcolsep}{0in}

        % Sections formatting
        \titleformat{\section}{
        \vspace{-4pt}\scshape\raggedright\large\bfseries
        }{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

        % Ensure that generate pdf is machine readable/ATS parsable
        \pdfgentounicode=1

        %-------------------------
        % Custom commands
        \newcommand{\resumeItem}[1]{
        \item\small{
            {#1 \vspace{-1pt}}
        }
        }

        \newcommand{\classesList}[4]{
            \item\small{
                {#1 #2 #3 #4 \vspace{-2pt}}
        }
        }

        \newcommand{\resumeSubheading}[4]{
        \vspace{-2pt}\item
            \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
            \textbf{\large#1} & \textbf{\small #2} \\
            \textit{\large#3} & \textit{\small #4} \\
            
            \end{tabular*}\vspace{-7pt}
        }


        \newcommand{\resumeSingleSubheading}[4]{
        \vspace{-2pt}\item
            \begin{tabular*}{1.0\textwidth}[t]{l@{\extracolsep{\fill}}r}
            \textbf{\large#1} & \textbf{\small #2} \\
            
            \end{tabular*}\vspace{-7pt}
        }

        \newcommand{\resumeSubSubheading}[2]{
            \item
            \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
            \textit{\small#1} & \textit{\small #2} \\
            \end{tabular*}\vspace{-7pt}
        }


        \newcommand{\resumeProjectHeading}[2]{
            \item
            \begin{tabular*}{1.001\textwidth}{l@{\extracolsep{\fill}}r}
            \small#1 & \textbf{\small #2}\\
            \end{tabular*}\vspace{-7pt}
        }

        \newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

        \renewcommand\labelitemi{$\vcenter{\hbox{\tiny$\bullet$}}$}
        \renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

        \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.0in, label={}]}
        \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
        \newcommand{\resumeItemListStart}{\begin{itemize}[leftmargin=0.1in]}
        \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}

        \newcommand\sbullet[1][.5]{\mathbin{\vcenter{\hbox{\scalebox{#1}{$\bullet$}}}}}

        %-------------------------------------------
        %%%%%%  RESUME STARTS HERE  %%%%%%%%%%%%%%%%%%%%%%%%%%%%


        \begin{document}
        %----------HEADING----------


        \begin{center}
            {\huge """ + fullname + r"""} \\ \vspace{8pt}
            {""" + socials['contact'] + r"""} ~ 
            \small{-}"""
    
    try:
        if socials['website'] :
            latex_setup += r"""
                    \href{""" + socials['website'] + r"""}{\color{blue}{Website}} ~ 
                    \small{-}"""
    except Exception as e:
        latex_setup += ""
    
    latex_setup += r"""
            \href{mailto:[""" + socials['mail'] + r"""]}{\color{blue}{""" + socials['mail'] + r"""}} ~ 
            \small{-}
            \href{[""" + socials['linkedin'] + r"""]}{ \color{blue}{Linkedin}}  ~
            \small{-}
            \href{[""" + socials['github'] + r"""]}{ \color{blue}{Github}} ~
            \vspace{-7pt}
        \end{center}
        """
    
    # --------------------- OBJECTIVE / SUMMARY ----------------------

    summary_latex = r"""\section{\color{airforceblue}SUMMARY}"""

    summary_entry = r"""
        """ + objective + r"""
        """
    summary_latex += summary_entry

    # --------------------- EDUCATION ----------------------

    education_latex = r"""
        %-----------EDUCATION-----------
        \section{\color{airforceblue}EDUCATION}
        \resumeSubHeadingListStart
        """

    education_entries = ""
    for edu in education:
        education_entries += r"""
            \resumeSubheading
            {""" + edu['institution'] + r"""}{""" + edu['grade'] + r"""}
            {""" + edu['qualification'] + r"""}{""" + edu['time'] + r"""}
            \vspace{2pt}
        """
    education_entries += r"""
        \resumeSubHeadingListEnd
        \vspace{-16pt}
        """
    
    education_latex += education_entries

    # --------------------- PROJECTS ----------------------

    projects_latex = r"""
        %-----------PROJECTS-----------
        \section{\color{airforceblue}PROJECTS}    
            \resumeItemListStart
                \vspace{0.5pt}
        """

    project_entries = ""
    for proj in projects:
        project_entries += r"""
                \resumeItem{\normalsize{\textbf{""" + proj['project_title'] + r"""}}}
                \hfill
                \textbf{""" + proj['tech'] + r"""}\\
                """ + proj['desc'] + r"""
        """
    project_entries += r"""
            \resumeItemListEnd  
        \vspace{-12pt}
        """
    
    projects_latex += project_entries

    # --------------------- SKILLS AND TECHNOLOGIES ----------------------

    skills_latex = r"""
        %-----------SKILLS AND TECHNOLOGIES-----------
        \section{\color{airforceblue}SKILLS AND TECHNOLOGIES}
        """

    skills_entries = ""
    for skill in skills:
        skills_entries += skill + ", "
    skills_entries = skills_entries.rstrip(", ") + ".\n"

    skills_latex += (skills_entries + r"\vspace{-6pt}" + "\n")


    # --------------------- PROGRAMMING LANGUAGES ----------------------

    languages_latex = r"""
        %-----------PROGRAMMING LANGUAGES-----------
        \section{\color{airforceblue}LANGUAGES}
        """

    languages_entries = ""
    for language in languages:
        languages_entries += language + ", "
    languages_entries = languages_entries.rstrip(", ") + ".\n"

    languages_latex += (languages_entries + r"\vspace{-6pt}" + "\n")


    # --------------------- COURSE WORK ----------------------

    coursework_latex = r"""
        %-----------COURSE WORK-----------
        \section{\color{airforceblue}COURSE WORK}
        """
    
    coursework_latex += (coursework + r"\vspace{-6pt}" + "\n")


    # --------------------- WORK EXPERIENCE ----------------------

    work_experience_latex = ""

    if len(work_experience) != 0:
        work_experience_latex = r"""
            %-----------EXPERIENCE-----------
            \section{\color{airforceblue}WORK EXPERIENCE}
                \resumeItemListStart
            """

        work_experience_entries = ""
        for work in work_experience:
            work_experience_entries += r"""
                        \resumeItem{\normalsize{""" + work + r"""}}  
            """
        work_experience_entries += r"""
                \resumeItemListEnd  
            \vspace{-12pt}
            """
        
        work_experience_latex += work_experience_entries


    # --------------------- PUBLICATIONS ----------------------

    publications_latex = ""

    if len(publications) != 0:
        publications_latex = r"""
            %-----------Publications---------------
            \section{\color{airforceblue}PUBLICATIONS}
                
            \resumeItemListStart
            """

        publications_entries = ""
        for pub in publications:
            publications_entries += r"""
                \resumeItem{\normalsize{""" + pub + r"""}}  
                \vspace{-5pt}
            """
        if not publications_entries:
            publications_entries = r"""
                \resumeItem{\normalsize{No publications yet.}}  
                \vspace{-5pt}
            """
        publications_entries += r"""
            \resumeItemListEnd 
                
            \vspace{-8pt}
            """
    
        publications_latex += publications_entries


    # --------------------- ADDITIONAL ENGAGEMENTS ----------------------

    additionals_latex = ""

    if len(additionals_latex) != 0:
        additionals_latex = r"""
            %-----------EXTRACURRICULAR---------------
            \section{\color{airforceblue}NON-TECHNICAL ACTIVITIES}
                
                \resumeItemListStart
            """

        extracurricular_entries = ""
        for additional in additionals:
            extracurricular_entries += r"""
                    \resumeItem{\normalsize{""" + additional + r"""}}  
                    \vspace{-5pt}
            """
        extracurricular_entries += r"""
                \resumeItemListEnd 
                
            \vspace{-8pt}
            """
        
        additionals_latex += extracurricular_entries


    # --------------------- ACHIEVEMENTS ----------------------

    achievements_latex = ""

    if len(achievements) != 0:
        achievements_latex = r"""
            \section{\color{airforceblue}ACHIEVEMENTS}
                \resumeItemListStart
            """

        achievements_entries = ""
        for achievement in achievements:
            achievements_entries += r"""
                    \resumeItem{\normalsize{""" + achievement + r"""}}  
                    \vspace{-5pt}
            """
        achievements_entries += r"""
                \resumeItemListEnd 

            \vspace{-8pt}
            """
        
        achievements_latex += achievements_entries


    # --------------------- CERTIFICATIONS ----------------------

    certifications_latex = ""

    if len(certifications) != 0:
        certifications_latex = r"""
            \section{\color{airforceblue}CERTIFICATIONS}
                \resumeItemListStart
            """

        certifications_entries = ""
        for certification in certifications:
            certifications_entries += r"""
                    \resumeItem{\normalsize{""" + certification + r"""}}  
                    \vspace{-5pt}
            """
        certifications_entries += r"""
            \resumeItemListEnd 
            \vspace{-8pt}"""

        certifications_latex += certifications_entries

    # --------------------- HOBBIES AND INTERESTS ---------------------- 

    hobbies_latex = r"""       
        %-----------HOBBIES-----------
        \section{\color{airforceblue}HOBBIES}""" + hobbies + r"""
        \vspace{-6pt}
        
        \end{document}
        """

    latex_document = (latex_setup + summary_latex + education_latex + projects_latex + skills_latex +
                      languages_latex + coursework_latex + work_experience_latex + publications_latex +
                      additionals_latex + achievements_latex + certifications_latex + hobbies_latex)

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
