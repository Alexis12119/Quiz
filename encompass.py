from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QEvent, QTimer, QUrl
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton, QStackedWidget, QHBoxLayout, QScrollArea
import time
from pathlib import Path


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.logo_label = QLabel("Image")
        # Set the path to your logo image
        self.logo_label.setPixmap(QPixmap(str(Path.home()) + '/Quiz/logo.png'))
        # Align the logo label to the center
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.student_id_label = QLabel("Student ID:")
        self.student_id_input = QLineEdit()
        self.student_id_label.setFont(QFont("Arial", 10))
        self.student_id_input.setFont(QFont("Arial", 10))
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        # Set password input to hide characters
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_label.setFont(QFont("Arial", 10))
        self.password_input.setFont(QFont("Arial", 12))
        self.login_button = QPushButton("Sign In")

        self.forgot_password_button = QPushButton("Made by Alexis Corporal")
        self.login_status = QLabel()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)  # Align the layout to the center

        layout.addWidget(self.logo_label)  # Add the logo label to the layout

        input_layout = QVBoxLayout()
        # Align the input layout to the center
        input_layout.setAlignment(Qt.AlignCenter)
        input_layout.addWidget(self.student_id_label)
        # Set maximum width for the student ID input
        self.student_id_input.setMaximumWidth(250)
        input_layout.addWidget(self.student_id_input)
        input_layout.addWidget(self.password_label)
        # Set maximum width for the password input
        self.password_input.setMaximumWidth(250)
        input_layout.addWidget(self.password_input)
        layout.addLayout(input_layout)
        # Set maximum width for the sign-in button
        self.login_button.setMaximumWidth(200)
        # Set maximum width for the forgot password button
        self.forgot_password_button.setMaximumWidth(200)

        button_layout = QVBoxLayout()
        # Align the button layout to the center
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.addWidget(self.login_button)
        button_layout.addSpacing(5)  # Add spacing between buttons
        button_layout.addWidget(self.forgot_password_button)
        layout.addLayout(button_layout)

        layout.addWidget(self.login_status)

        self.student_id_input.installEventFilter(self)
        self.password_input.installEventFilter(self)

        # Set font color to white
        self.setStyleSheet("background-color: black; color: white;")

    def eventFilter(self, obj, event):
        if obj is self.student_id_input and event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            if self.student_id_input.text() == "":
                self.password_input.setFocus()
            else:
                self.password_input.setFocus()
                return True
        elif obj is self.password_input and event.type() == QEvent.KeyPress and event.key() == Qt.Key_Return:
            if self.password_input.text() == "":
                self.student_id_input.setFocus()
            else:
                login()
                return True
        return super().eventFilter(obj, event)


def login():
    student_id = login_widget.student_id_input.text()
    password = login_widget.password_input.text()

    if student_id == "" and password == "":
        login_widget.login_status.setText(
            "Please enter your Student ID and Password!")
    elif student_id == "abc" and password == "123":
        stacked_widget.removeWidget(login_widget)
        show_choice_window()
    else:
        login_widget.login_status.setText("Invalid student ID or password.")

    # Center align the text in login_status QLabel
    login_widget.login_status.setAlignment(Qt.AlignCenter)


def show_choice_window():
    choice_widget = QWidget()

    choice_layout = QVBoxLayout(choice_widget)

    choice_label = QLabel("Welcome! Choose an option:")
    choice_label.setStyleSheet("font-size: 20px; color: white;")
    choice_layout.addWidget(choice_label)

    # Align the button layout to the center
    choice_layout.setAlignment(Qt.AlignCenter)
    choice_layout.addStretch()

    sri_button = QPushButton("SRI (Silent Recruiting Inventory)")
    sri_button.setStyleSheet("QPushButton { font-size: 18px; width: 500px; height: 200px; background-color: gray; color: white; }"
                             "QPushButton:hover { background-color: lightblue; color: black; }")
    sri_button.clicked.connect(show_grade_buttons)
    choice_layout.addWidget(sri_button)

    remedial_button = QPushButton("Remedial")
    remedial_button.setStyleSheet("QPushButton { font-size: 18px; width: 100px; height: 200px; background-color: gray; color: white; }"
                                  "QPushButton:hover { background-color: lightblue; color: black; }")
    remedial_button.clicked.connect(display_remedial_article)
    choice_layout.addWidget(remedial_button)

    choice_layout.addStretch()

    stacked_widget.addWidget(choice_widget)
    stacked_widget.setCurrentWidget(choice_widget)


def show_grade_buttons():
    grade_widget = QWidget()
    grade_layout = QVBoxLayout(grade_widget)

    grade_label = QLabel("Choose a grade:")
    grade_label.setStyleSheet("font-size: 20px; color: white;")
    grade_layout.addWidget(grade_label)

    grade_layout.addStretch()

    button_layout = QHBoxLayout()
    # Align the button layout to the center
    button_layout.setAlignment(Qt.AlignCenter)

    grade_11_button = QPushButton("Grade 11")
    grade_11_button.setStyleSheet("QPushButton { font-size: 18px; width: 300px; height: 200px; background-color: gray; color: white; }"
                                  "QPushButton:hover { background-color: lightblue; color: black; }")
    # Connect the Grade 11 button to show the start screen
    grade_11_button.clicked.connect(display_grade_11_article)
    button_layout.addWidget(grade_11_button)

    grade_12_button = QPushButton("Grade 12")
    grade_12_button.setStyleSheet("QPushButton { font-size: 18px; width: 300px; height: 200px; background-color: gray; color: white; }"
                                  "QPushButton:hover { background-color: lightblue; color: black; }")
    # Connect the Grade 12 button to show the start screen
    grade_12_button.clicked.connect(display_grade_12_article)
    button_layout.addWidget(grade_12_button)

    grade_layout.addLayout(button_layout)

    grade_layout.addStretch()

    back_button = QPushButton("Back")
    back_button.clicked.connect(show_choice_window)
    back_button.setStyleSheet("QPushButton { font-size: 18px; width: 100px; height: 50px; background-color: gray; color: white; }"
                              "QPushButton:hover { background-color: lightblue; color: black; }")
    grade_layout.addWidget(back_button)

    stacked_widget.addWidget(grade_widget)
    stacked_widget.setCurrentWidget(grade_widget)

def display_article(article_text, max_time, next_button_callback, questions_callback):
    bg_music = str(Path.home()) + "/Quiz/clock.mp3"
    # Create the media player
    player = QMediaPlayer()

    def play_background_music():
        # Load the background music file
        media_url = QUrl.fromLocalFile(bg_music)
        media_content = QMediaContent(media_url)
        player.setMedia(media_content)
        # Start playing the background music
        player.play()

    def restart_background_music():
        player.setPosition(0)  # Reset the position to the beginning
        player.play()

    player.mediaStatusChanged.connect(lambda status: restart_background_music() if status == QMediaPlayer.EndOfMedia else None)


    timer_label = QLabel()
    timer_label.setStyleSheet("QLabel { font-size: 20px; color: white; }")

    article_widget = QWidget()
    article_layout = QVBoxLayout(article_widget)

    article_layout.addWidget(timer_label, alignment=Qt.AlignBottom)

    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    article_widget_inner = QWidget()
    article_layout_inner = QVBoxLayout(article_widget_inner)

    article_label = QLabel(article_text)
    article_label.setStyleSheet("color: white; font-size: 20px;")

    article_layout_inner.addWidget(article_label)
    scroll_area.setWidget(article_widget_inner)

    article_layout.addWidget(scroll_area)

    next_button = QPushButton("Next")
    next_button.setStyleSheet("QPushButton { font-size: 14px; width: 50px; height: 60px; background-color: gray; color: white; }"
                              "QPushButton:hover { background-color: lightblue; color: black; }")
    article_layout.addWidget(
        next_button, alignment=Qt.AlignBottom | Qt.AlignRight)
    next_button.clicked.connect(next_button_callback)
    next_button.clicked.connect(player.stop)

    stacked_widget.addWidget(article_widget)
    stacked_widget.setCurrentWidget(article_widget)

    def update_timer():
        elapsed_time = int(time.time() - start_time)
        time_remaining = max(0, max_time - elapsed_time)
        minutes = time_remaining // 60
        seconds = time_remaining % 60
        timer_label.setText(f"Time Remaining: {minutes:02d}:{seconds:02d}")
        if time_remaining == 0:
            timer.stop()
            player.stop()
            questions_callback()
        if time_remaining == 10:
            play_background_music()

    start_time = time.time()
    timer = QTimer()
    timer.timeout.connect(update_timer)
    timer.start(1000)

def show_questions(grade, questions):
    question_index = 0
    correct_answers = 0

    bg_music = str(Path.home()) + "/Quiz/thinking.mp3"
    # Create the media player
    player = QMediaPlayer()

    def play_background_music():
        # Load the background music file
        media_url = QUrl.fromLocalFile(bg_music)
        media_content = QMediaContent(media_url)
        player.setMedia(media_content)
        # Start playing the background music
        player.play()

    def restart_background_music():
        player.setPosition(0)  # Reset the position to the beginning
        player.play()

    player.mediaStatusChanged.connect(lambda status: restart_background_music() if status == QMediaPlayer.EndOfMedia else None)

    play_background_music()
    def next_question():
        nonlocal question_index
        if question_index < len(questions):
            question = questions[question_index]
            display_question_window(question)
            question_index += 1
        else:

            show_results(grade, correct_answers)
            player.stop()

    def display_question_window(question):
        question_widget = QWidget()
        question_layout = QVBoxLayout(question_widget)

        question_label = QLabel(question["question"])
        question_label.setStyleSheet("font-size: 20px; color: white;")
        question_layout.addWidget(question_label)

        choice_layout = QVBoxLayout()
        for choice_index, choice in enumerate(question["choices"]):
            choice_button = QPushButton(choice)
            choice_button.setStyleSheet("QPushButton { font-size: 18px; width: 400px; height: 80px; background-color: #71BAF2; color: black; border-radius: 10px; }"
                                        "QPushButton:hover { background-color: #1a91ff; }")
            choice_button.setFont(QFont("Arial", 11))

            def choice_selected(choice_index):
                nonlocal correct_answers
                if choice_index == ord(question["answer"]) - ord('a'):
                    # Correct answer selected
                    correct_answers += 1

                next_question()

            choice_button.clicked.connect(
                lambda _, choice_index=choice_index: choice_selected(choice_index))
            choice_layout.addWidget(choice_button)

        question_layout.addLayout(choice_layout)

        stacked_widget.addWidget(question_widget)
        stacked_widget.setCurrentWidget(question_widget)

    def show_results(grade, correct_answers):
        bg_music = str(Path.home()) + "/Quiz/claps.mp3"
        # Create the media player
        player = QMediaPlayer()

        def play_background_music():
            # Load the background music file
            media_url = QUrl.fromLocalFile(bg_music)
            media_content = QMediaContent(media_url)
            player.setMedia(media_content)
            # Start playing the background music
            player.play()

        def restart_background_music():
            player.setPosition(0)  # Reset the position to the beginning
            player.play()

        player.mediaStatusChanged.connect(lambda status: restart_background_music() if status == QMediaPlayer.EndOfMedia else None)

        play_background_music()


        results_widget = QWidget()
        results_layout = QVBoxLayout(results_widget)

        results_label = QLabel(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
        results_label.setStyleSheet("font-size: 24px; color: white;")
        results_label.setAlignment(Qt.AlignCenter)  # Align the text to the center
        results_layout.addWidget(results_label)


        # Display different messages based on the number of correct answers
        if correct_answers == len(questions):
            result_message = "You nailed it!"
        elif correct_answers == 0:
            result_message = "Better luck next time"
        else:
            result_message = "Nice Try"

        result_message_label = QLabel(result_message)
        result_message_label.setStyleSheet("font-size: 24px; color: white;")
        result_message_label.setAlignment(Qt.AlignCenter)  # Align the text to the center
        results_layout.addWidget(result_message_label)

        stacked_widget.addWidget(results_widget)
        stacked_widget.setCurrentWidget(results_widget)

        main_menu_button = QPushButton("Main Menu")
        main_menu_button.setStyleSheet("QPushButton { font-size: 24px; width: 150px; height: 60px; background-color: gray; color: white; }"
                                       "QPushButton:hover { background-color: lightblue; color: black; }")
        results_layout.addWidget(main_menu_button, alignment=Qt.AlignBottom | Qt.AlignRight)

        

        main_menu_button.clicked.connect(show_choice_window)
        main_menu_button.clicked.connect(player.stop)
    next_question()

def create_button(text, clicked_callback):
    button = QPushButton(text)
    button.setStyleSheet("QPushButton { font-size: 24px; width: 200px; height: 100px; background-color: #00b8ff; color: white; border-radius: 10px; }"
                         "QPushButton:hover { background-color: #1a91ff; }")
    button.setFont(QFont("Arial", 16))
    button.clicked.connect(clicked_callback)
    return button

def create_start_widget(start_button_text, questions_callback):
    start_widget = QWidget()
    start_layout = QVBoxLayout(start_widget)

    start_button = create_button(start_button_text, questions_callback)
    start_layout.addWidget(start_button)

    stacked_widget.addWidget(start_widget)
    stacked_widget.setCurrentWidget(start_widget)

def show_remedial_start():
    create_start_widget("Start Remedial", show_remedial_questions)

def show_remedial_questions():
    questions = [
        {
            "question": """
        1. What are 'nociceptors'?
        """,
            "choices": ["Electrical impulses", "Memories of pain", "Nerve receptors", "Sensations of pain"],
            "answer": "c"
        },
        {
            "question": """
        2. How do memories of pain help us?
        """,
            "choices": ["Constantly remind us of what hurts", "Help dull the senses", "Help us re-experience the pain", "Inform us on what to watch out for"],
            "answer": "d"
        },
        {
            "question": """
        3. Suffering is the complex mix of ________________.
        """,
            "choices": ["Physical, mental and spiritual experiences", "Physical, psychological and social influences", "Physical, sociological and cognitive factors", "Physical, emotional and psychological experiences"],
            "answer": "d"
        },
        {
            "question": """
        4. Which of the following is an example of how memories of pain help us?
        """,
            "choices": ["A baby crying at the sight of the needle", "Drinking a painkiller once a headache starts", "Asking if a dental procedure will hurt", "We relive these experiences through our dreams"],
            "answer": "b"
        },
        {
            "question": """
        5. Which is an example of helping the body avoid the creation of 
        memories for pain?
        """,
            "choices": ["Avoiding the use of anesthesia", "Drinking a painkiller once a headache starts", "Talking about a painful experience with a friend", "Being given an anesthetic before a dental procedure"],
            "answer": "d"
        },
        {
            "question": """
        6. In the selection, how was the word 'chronic' used in the phrase “chronic pain"?
        """,
            "choices": ["Continuous", "In-born", "Throbbing", "Worsening"],
            "answer": "a"
        },
        {
            "question": """
        7. Which of the following adjectives best describes our 
        memories’ role in managing pain?
        """,
            "choices": ["Curative", "Corrective", "Preventive", "Restorative"],
            "answer": "c"
        },
        {
            "question": """
        8. In the selection, what does it mean to ‘sense pain’?
        """,
            "choices": ["Create pain", "Recognize pain", "Remember pain", "Understand pain"],
            "answer": "b"
        }
    ]
    show_questions("Remedial", questions)


def display_remedial_article():
    article_text = """
    PAIN

    How do we sense pain? The human body has nociceptors to 
    receive an electrical impulse that is sent to part of 
    the brain that recognizes pain. Memories of these sensations 
    are formed to help us avoid painful objects and experiences
    and prevents us from repeating past mistakes that may have
    hurt us in some way. But pain is more complex. It is not only
    a physical experience but an emotional and psychological one 
    as well. When all of these come together, it is called suffering.
    The mind is not alone in recognizing pain. The nervous system 
    is also able to store such information. Even when a person loses 
    a finger or a limb, the pain that was once felt may become a 
    chronic one – one that keeps recurring. The best way to avoid 
    this is to prevent pain memories from forming. The use of 
    anesthesia prevents the mind from creating these memories. 
    Drugs that prevent pain such as analgesics help lessen the 
    pain sensed.
    """
    display_article(article_text, 60, show_remedial_start, show_remedial_questions)

def show_grade_11_start():
    create_start_widget("Start Quiz", show_grade_11_questions)

def show_grade_11_questions():
    questions = [
        {
            "question": """
        1. Most migrant animals
        """,
            "choices": ["Make a round-trip each year", "Make a round-trip once in their life cycle", "Die after they migrate"],
            "answer": "a"
        },
        {
            "question": """
        2. Most animals migrate because of
        """,
            "choices": ["Boredom", "Food availability and seasonal changes", "A need to return home"],
            "answer": "b"
        },
        {
            "question": """
        3. Migrating birds usually travel
        """,
            "choices": ["Wherever the wind takes them", "Alone", "Over specific, well-defined routes"],
            "answer": "c"
        },
        {
            "question": """
        4. The most characteristic migratory formation for birds is the
        """,
            "choices": ["A-formation", "V-formation", "W-formation"],
            "answer": "b"
        },
        {
            "question": """
        5. In some species, the male birds migrate before the females so that they can
        """,
            "choices": ["Select the nesting site", "Fend off enemies", "Stockpile food"],
            "answer": "a"
        },
        {
            "question": """
        6. If climate and food supply remained constant, most animals would probably
        """,
            "choices": ["Stay in one place", "Continue to migrate", "Change their eating habits"],
            "answer": "a"
        },
        {
            "question": """
        7. From the selection, you can conclude that many birds of prey usually
        """,
            "choices": ["Hunt alone", "Live in large flocks", "Migrate alone"],
            "answer": "b"
        },
        {
            "question": """
        8. Even small birds can fly over vast amounts of water during migration, 
        which suggests that
        """,
            "choices": ["There is a strong correlation between size and endurance", "Smaller birds have more endurance than larger birds", "Size and endurance are not related"],
            "answer": "c"
        },
        {
            "question": """
        9. Whether male and female birds migrate together depends on
        """,
            "choices": ["Breeding habits", "Flying ability", "Location north"],
            "answer": "a"
        },
        {
            "question": """
        10. Birds migrate over specific routes, which suggests that
        """,
            "choices": ["All migrating animals follow the same routes", "Birds are able to remember previous migrations", "Migrations are dependent on geographic features"],
            "answer": "c"
        }
    ]

    show_questions("Grade 11", questions)


def display_grade_11_article():
    article_text = """
    Go with the Flow

    Many people take seasonal trips In search of a fair climate,
    good food, and a change of scene in pleasant surroundings.
    Some animals are impelled to travel for similar reasons. Their 
    trips, too, are often annual and linked to the seasons. As
    the season change, they migrate to find food. These traveling 
    animals are called migrants, and their trips are called migrations.
    Most kinds of migrant animals make a round-trip each year. Grazing 
    animals, particularly the hoofed animals of eastern Africa and the 
    Arctic Tundra, follow the seasonal changes in their search for green
    plants. Even fishes migrate. Some travel seasonally, and some travel
    less often. For example, eels and many salmon make a round-trip only 
    once in their life cycle. These animals return to the home waters
    where they were born to lay eggs, and then they usually die. 
    Some animals make some long journeys back and forth across land 
    and ocean. Other migrations, however, take a vertical direction. 
    During seasons of severe weather in mountainous regions, for instance, 
    certain birds, Insects, and mammals make regular trips from their breeding
    grounds in high altitudes into the foothills or plains below. 

    Many birds become gregarious during their travels. Even those that are 
    fiercely individualistic at other times, such as birds of prey and those 
    that hunt insects, often travel with birds that have similar habits. 
    Large migrating flocks may be seen scattered along a broad flyway hundreds 
    of miles wide. Often the birds show remarkable groupings. The most 
    characteristic migratory formation is the V-shape of a flock of geese, 
    ducks, pelicans, or cranes, the V pointed in the direction of the flight. 
    Birds usually follow specific, well-defined routes over long distances 
    marked by rivers, valleys, coasts, forests, plains, deserts, and other 
    geographic features. However, birds may change routes because of wind and
    weather. The routes of some of the larger birds span oceans. Even small 
    birds may cross as many as 1,000 miles (1,600 kilometers) of water 
    over the Gulf of Mexico, the Mediterranean Sea, or the North Sea. 

    In the fall, female shorebirds often depart first, leaving the males to 
    care for the young. In other species, male birds migrate first. They 
    fly ahead to select the nesting site in preparation for the arrival of 
    the females. Sometimes, males and females travel together and may choose 
    mates along the way. Geese, which mate for life, travel as couples in
    large flocks.
    """

    display_article(article_text, 300, show_grade_11_start, show_grade_11_questions)


def show_grade_12_start():
    create_start_widget("Start Quiz", show_grade_12_questions)

def show_grade_12_questions():
    questions = [
        {
            "question": """
        1. In the United States, alcoholism affects
        """,
            "choices": ["Adults only", "At least 5 million persons", "Most people"],
            "answer": "b"
        },
        {
            "question": """
        2. One-half of all fatal automobile accidents each year 
        are caused by
        """,
            "choices": ["Teenagers", "Bad weather", "Drunk drivers"],
            "answer": "c"
        },
        {
            "question": """
        3. Scientific research suggests that alcohol abuse
        """,
            "choices": ["Ruins families", "Is most frequent in rural areas", "Leads to drug addiction"],
            "answer": "a"
        },
        {
            "question": """
        4. Antabuse helps prevent drinking by
        """,
            "choices": ["Eliminating the desire to drink", "Causing a violent physical reaction when alcohol is consumed", "Inhibiting the alcoholic's mental function"],
            "answer": "a"
        },
        {
            "question": """
        5. Alcohol abuse causes cirrhosis, or damage to the
        """,
            "choices": ["Nervous system", "Brain", "Liver"],
            "answer": "c"
        },
        {
            "question": """
        6. The article suggests that recovery from alcoholism depends mainly on
        """,
            "choices": ["Whether the disease is inherited", "The alcoholic's decision to stop drinking", "Resources available to the alcoholic"],
            "answer": "b"
        },
        {
            "question": """
        7. You can conclude from the article that alcoholics
        """,
            "choices": ["Can limit their drinking", "Suffer no physical harm from drinking", "Can cause problems for families and friends"],
            "answer": "a"
        },
        {
            "question": """
        8. You can conclude from the article that the effects of alcoholism
        """,
            "choices": ["Are primarily physical", "Include physical, economic, and social problems", "Are not very important"],
            "answer": "b"
        },
        {
            "question": """
        9. Alcoholism is the most widespread form of drug abuse in the United States,
        which suggests that
        """,
            "choices": ["Most Americans are problem drinkers", "Americans need to be better educated about the harmful effects of alcohol", "People in the United States should not be allowed to drink alcohol"],
            "answer": "a"
        },
        {
            "question": """
        10. You can conclude from the article that causes of alcoholism are
        """,
            "choices": ["Well understood", "Still being researched", "Usually psychological"],
            "answer": "a"
        }
    ]
    show_questions("Grade 12", questions)


def display_grade_12_article():
    article_text = """
    Problem Drinking

    An overwhelming desire to drink alcohol is a disease called 
    alcoholism. Alcohol is a drug; it causes harm. In the United States,
    alcoholism is the most widespread form of drug abuse. Alcoholism
    affects at least 5 million persons. About one third of high school
    students in the United States are thought to be problem drinkers.
    Many may be alcoholics. Drunk drivers account for one-half of all
    fatal automobile accidents each year. Drinking is a leading cause 
    of loss of income. Heavy drinkers display social and personal problems.
    
    Alcoholism also creates many severe physical problems. More than
    three drinks a day over even a few weeks causes destructive changes 
    in the liver. About 15 percent of heavy drinkers develop cirrhosis,
    a liver disease that can be fatal. Changes in the brain and nervous 
    system result in hostile behavior, loss of mental sharpness, and poor
    judgment. One-third of the babies born to mothers who drink heavily 
    have birth defects or retardation. This condition is called fetal 
    alcohol syndrome. Some drugs, such as tranquilizers, when taken with 
    alcohol can result in death. It has long been thought that alcohol
    abuse resulted from a combination of psychological and social factors.
    
    Current scientific research suggests that a tendency to abuse alcohol
    runs in families. An inherited chemical defect could play a role.
    Researchers have discovered a rare gene, possibly one of several that 
    may lead to alcoholism. This suggests that in some cases the disease 
    may be inherited. A family or individual with an alcohol problem is 
    in serious trouble. The alcoholic's main goal is to get something to 
    drink. The drinking usually continues until the victim is drunk. Family,
    work, and friends are of little concern when there is a need for alcohol. 
    Drunkenness inhibits the alcoholic's control of normal behavior. 
    It depresses the ability to perform even the simplest functions. 
    Alcoholics can be helped. Two absolute rules apply to their recovery. 
    An alcoholic must accept the fact that there a real problem and decide 
    to stop drinking. Second, the patient must also realize that any form 
    or quantity of alcohol is literally poison. Most treatment experts believe
    that an alcoholic can never take another drink. Alcoholism is a lifelong 
    condition. Since the late 1940's, Antabuse and other drugs have been 
    used to prevent drinking. The drug causes a violent physical reaction when
    alcohol is consumed. Problem drinkers can and are being helped.
    """

    display_article(article_text, 300, show_grade_12_start, show_grade_12_questions)


app = QApplication([])

# Create the main window
main_window = QMainWindow()
main_window.setWindowTitle("Encompass")

# Create login page widget
login_widget = LoginWidget()

login_widget.login_button.clicked.connect(login)

# Create stacked widget
stacked_widget = QStackedWidget()
stacked_widget.addWidget(login_widget)

main_window.setCentralWidget(stacked_widget)

# Set window size and center it on the screen
window_width = 800
window_height = 700
screen_geometry = QApplication.desktop().screenGeometry()
x = (screen_geometry.width() - window_width) // 2
y = (screen_geometry.height() - window_height) // 2
main_window.setGeometry(x, y, window_width, window_height)

# Set main window background color to black
main_window.setStyleSheet("background-color: black;")

# Set the window icon
# Replace "path_to_icon_file.png" with the actual path to your icon file
icon = QIcon(str(Path.home())+ "/Quiz/logo.png")
main_window.setWindowIcon(icon)

# Show the window
main_window.show()

app.exec_()
