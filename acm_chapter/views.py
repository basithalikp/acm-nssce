from django.shortcuts import render
from django.templatetags.static import static

# Hardcoded data for simplicity
# --- EVENT DATA ---
event_data = [
    {'title': 'Algorithmic Sprint 2025', 'date': 'Oct 15, 2025', 'desc': 'A 24-hour competitive python programming marathon. Sharpen your algorithmic thinking with python skills.', 'image': 'https://images.unsplash.com/photo-1542831371-29b0f74f9713?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=1200'},
    {'title': 'AI & ML Workshop', 'date': 'Nov 02, 2025', 'desc': 'Dive into the world of Artificial Intelligence with hands-on sessions on TensorFlow and PyTorch.', 'image': static('acm_chapter/images/AIandML.jpg')},
    {'title': 'CyberSec Summit', 'date': 'Nov 18, 2025', 'desc': 'Learn about ethical hacking, network security, and cryptography from industry experts.', 'image': static('acm_chapter/images/cyberSecurity.jpg')},
    {'title': 'Intro to Django', 'date': 'Dec 05, 2025', 'desc': 'Build and deploy your first web application with Python and Django. A beginner-friendly workshop.', 'image': static('acm_chapter/images/introToDjango.jpg')},
    {'title': 'UI/UX Design Principles', 'date': 'Jan 10, 2026', 'desc': 'Master the fundamentals of user interface and user experience design with Figma.', 'image': static('acm_chapter/images/uiUxDesignPrinciples.jpg')},
    {'title': 'Cloud Computing with AWS', 'date': 'Feb 22, 2026', 'desc': 'Explore cloud services and infrastructure with Amazon Web Services (AWS).', 'image': static('acm_chapter/images/cloudComputing.jpg')},
]

# --- TEAM DATA ---
team_data = {
    'advisor': {'name': 'Dr. Syam Sankar', 'role': 'Faculty Advisor', 'img': static('acm_chapter/images/syamSankar.png'), 'linkedin': 'https://www.linkedin.com/in/syam-sankar-134b70110/', 'github': 'https://syam-nssce.github.io/syamsankar/'},
    'core': [
        {'name': 'Bensen Biju', 'role': 'Chairperson', 'img': static('acm_chapter/images/members/bensenBiju.jpg'), 'linkedin': 'https://www.linkedin.com/in/bensen-biju-b12b78343', 'github': 'https://github.com/Bensen8806'},
        {'name': 'Anna Rose', 'role': 'Vice Chairperson', 'img': static('acm_chapter/images/members/annaRose.jpg'), 'linkedin': 'https://www.linkedin.com/in/anna-rose-8ab870329', 'github': 'https://github.com/annarosepynadath'},
        {'name': 'Christy Sebastian', 'role': 'Secretary', 'img': static('acm_chapter/images/members/christySebastian.jpg'), 'linkedin': 'https://www.linkedin.com/in/christy-sebastian-3b2582347?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app', 'github': 'https://github.com/Christy303'},
        {'name': 'Drisya A', 'role': 'Treasurer', 'img': static('acm_chapter/images/members/drisyaA.jpg'), 'linkedin': 'https://www.linkedin.com/in/dhrisya-a-594082339', 'github': 'https://github.com/dhrisyarevathy'},
    ],
    'tech': [
        {'name': 'Basith Ali KP', 'role': 'Tech Head, Web Master', 'img': static('acm_chapter/images/basithAliKP.jpg'), 'linkedin': 'https://www.linkedin.com/in/basithalikp/', 'github': 'https://github.com/basithalikp'},
        {'name': 'Rida Kareem', 'role': 'Tech Member, Web Dev', 'img': static('acm_chapter/images/members/ridaKareem.jpg'), 'linkedin': 'http://www.linkedin.com/in/rida-kareem', 'github': 'https://github.com/ridakareem'},
        {'name': 'Avaneesh R', 'role': 'Tech Member', 'img': static('acm_chapter/images/members/avaneeshR.png'), 'linkedin': 'https://www.linkedin.com/in/avaneesh-r-38183b348?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app', 'github': 'https://github.com/Avaneesh0625x'},
    ],
    'design': [
        {'name': 'Ayush R Kumar', 'role': 'Design Head', 'img': static('acm_chapter/images/members/ayushRKumar.jpg'), 'linkedin': 'https://www.linkedin.com/in/ayush-r-kumar-055478329/', 'github': 'https://github.com/Ayush2006385'},
        {'name': 'Angel SS', 'role': 'Design Member', 'img': static('acm_chapter/images/members/angelSS.jpg'), 'linkedin': 'https://www.linkedin.com/in/angel-s-s-988844348?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app', 'github': 'https://github.com/AngelSS921'},
        {'name': 'Aiswarya A', 'role': 'Design Member', 'img': static('acm_chapter/images/members/aiswaryaA.jpg'), 'linkedin': 'https://www.linkedin.com/in/aiswarya-a-829b1833a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app', 'github': 'https://github.com/aiswarya7033kvk-sys'},
        {'name': 'Aiswary MP', 'role': 'Design Member', 'img': static('acm_chapter/images/members/aiswaryaMp.jpg'), 'linkedin': 'https://www.linkedin.com/in/aiswarya-mp-29470a336?utm_source=share_via&utm_content=profile&utm_medium=member_android', 'github': 'https://github.com/aiswaryapradeep2005'},
    ],
    'membership': [
        {'name': 'Afrin Asif', 'role': 'Membership Chair', 'img': static('acm_chapter/images/members/afrinAsif.jpg'), 'linkedin': 'https://www.linkedin.com/in/afrin-asif-9b4a242a9/', 'github': 'https://github.com/afrinasif', 'phone': '94958 60051'},
        {'name': 'Aditi AM', 'role': 'Membership Advisor', 'img': 'https://i.pravatar.cc/300?u=mem2', 'linkedin': '#', 'github': '#', 'phone': '919876543211'},
    ],
    'media': [
        {'name': 'Anulakshmi C', 'role': 'Media Head', 'img': 'https://i.pravatar.cc/300?u=mediahead', 'linkedin': '#', 'github': '#'},
        {'name': 'Amna Sherin VA', 'role': 'Media Member', 'img': 'https://i.pravatar.cc/300?u=media1', 'linkedin': '#', 'github': '#'},
        {'name': 'Arunima N', 'role': 'Media Member', 'img': 'https://i.pravatar.cc/300?u=media1', 'linkedin': '#', 'github': '#'},
    ],
    'content': [
        {'name': 'Anaswara VK', 'role': 'Content Head', 'img': static('acm_chapter/images/members/anaswara.jpg'), 'linkedin': 'https://www.linkedin.com/in/anaswara-vk-11b839348?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app', 'github': 'https://github.com/AnaswaraKrishna00'},
        {'name': 'Anagha Gopalakrishnan', 'role': 'Content Writer', 'img': 'https://i.pravatar.cc/300?u=content1', 'linkedin': '#', 'github': '#'},
        {'name': 'Aryananda T', 'role': 'Content Writer', 'img': static('acm_chapter/images/members/aryananda.jpg'), 'linkedin': 'https://www.linkedin.com/in/aryananda-t-3bba2b327?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app', 'github': 'https://github.com/24b165-code'},
        {'name': 'Alaina Sanoj', 'role': 'Content Writer', 'img': static('acm_chapter/images/members/alainaSanoj.jpg'), 'linkedin': 'https://www.linkedin.com/in/alaina-sanoj-a4837b387?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app', 'github': 'https://github.com/alainasanoj00-hue'},
    ]
}

def home_view(request):
    context = {
        'page': 'home',
        'events': event_data[:4],  # Show first 4 events on home
        'team_leads': [
            team_data['advisor'],
            team_data['core'][0],  # Chair
            team_data['core'][2],  # Secretary
            team_data['core'][3],  # Treasurer
        ]
    }
    return render(request, 'acm_chapter/home.html', context)

def events_view(request):
    context = {
        'page': 'events',
        'events': event_data
    }
    return render(request, 'acm_chapter/events.html', context)

def team_view(request):
    context = {
        'page': 'team',
        'team': team_data
    }
    return render(request, 'acm_chapter/team.html', context)

def about_view(request):
    context = {
        'page': 'about',
        'advisors': team_data['membership'],
        'chairperson': {**team_data['core'][0], 'phone': '919876543212'}  # Add dummy phone
    }
    return render(request, 'acm_chapter/about.html', context)
