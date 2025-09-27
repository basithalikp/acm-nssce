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
    'advisor': {'name': 'Dr. Syam Sankar', 'role': 'Faculty Advisor', 'img': static('acm_chapter/images/syamSankar.png'), 'linkedin': 'https://www.linkedin.com/in/syam-sankar-134b70110/', 'github': '#'},
    'core': [
        {'name': 'Bensen Biju', 'role': 'Chairperson', 'img': 'https://i.pravatar.cc/300?u=chair', 'linkedin': '#', 'github': '#'},
        {'name': 'Anna Rose', 'role': 'Vice Chairperson', 'img': 'https://i.pravatar.cc/300?u=vicechair', 'linkedin': '#', 'github': '#'},
        {'name': 'Christy Sebastian', 'role': 'Secretary', 'img': 'https://i.pravatar.cc/300?u=secretary', 'linkedin': '#', 'github': '#'},
        {'name': 'Drisya A', 'role': 'Treasurer', 'img': 'https://i.pravatar.cc/300?u=treasurer', 'linkedin': '#', 'github': '#'},
    ],
    'tech': [
        {'name': 'Basith Ali KP', 'role': 'Tech Head', 'img': static('acm_chapter/images/basithAliKP.jpg'), 'linkedin': 'https://www.linkedin.com/in/basithalikp/', 'github': 'https://github.com/basithalikp'},
        {'name': 'Avaneesh R', 'role': 'Tech Member', 'img': 'https://i.pravatar.cc/300?u=tech1', 'linkedin': '#', 'github': '#'},
    ],
    'design': [
        {'name': 'Ayush R Kumar', 'role': 'Design Head', 'img': 'https://i.pravatar.cc/300?u=designhead', 'linkedin': '#', 'github': '#'},
        {'name': 'Angel SS', 'role': 'Design Member', 'img': 'https://i.pravatar.cc/300?u=design1', 'linkedin': '#', 'github': '#'},
        {'name': 'Aiswarya A', 'role': 'Design Member', 'img': 'https://i.pravatar.cc/300?u=design1', 'linkedin': '#', 'github': '#'},
        {'name': 'Aiswary MP', 'role': 'Design Member', 'img': 'https://i.pravatar.cc/300?u=design1', 'linkedin': '#', 'github': '#'},
    ],
    'membership': [
        {'name': 'Afrin Asif', 'role': 'Membership Chair', 'img': 'https://i.pravatar.cc/300?u=mem1', 'linkedin': '#', 'github': '#', 'phone': '919876543210'},
        {'name': 'Aditi AM', 'role': 'Membership Advisor', 'img': 'https://i.pravatar.cc/300?u=mem2', 'linkedin': '#', 'github': '#', 'phone': '919876543211'},
    ],
    'media': [
        {'name': 'Anulakshmi C', 'role': 'Media Head', 'img': 'https://i.pravatar.cc/300?u=mediahead', 'linkedin': '#', 'github': '#'},
        {'name': 'Amna Sherin VA', 'role': 'Media Member', 'img': 'https://i.pravatar.cc/300?u=media1', 'linkedin': '#', 'github': '#'},
        {'name': 'Arunima N', 'role': 'Media Member', 'img': 'https://i.pravatar.cc/300?u=media1', 'linkedin': '#', 'github': '#'},
    ],
    'content': [
        {'name': 'Anaswara VK', 'role': 'Content Head', 'img': 'https://i.pravatar.cc/300?u=contenthead', 'linkedin': '#', 'github': '#'},
        {'name': 'Anagha Gopalakrishnan', 'role': 'Content Writer', 'img': 'https://i.pravatar.cc/300?u=content1', 'linkedin': '#', 'github': '#'},
        {'name': 'Aryananda T', 'role': 'Content Writer', 'img': 'https://i.pravatar.cc/300?u=content1', 'linkedin': '#', 'github': '#'},
        {'name': 'Alaina Sanoj', 'role': 'Content Writer', 'img': 'https://i.pravatar.cc/300?u=content1', 'linkedin': '#', 'github': '#'},
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
