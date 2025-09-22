from django.shortcuts import render

# Hardcoded data for simplicity
# --- EVENT DATA ---
event_data = [
    {'title': 'CodeSprint 2025', 'date': 'Oct 15, 2025', 'desc': 'A 24-hour competitive programming marathon. Sharpen your algorithms and data structures skills.', 'image': 'https://images.unsplash.com/photo-1542831371-29b0f74f9713?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=1200'},
    {'title': 'AI & ML Workshop', 'date': 'Nov 02, 2025', 'desc': 'Dive into the world of Artificial Intelligence with hands-on sessions on TensorFlow and PyTorch.', 'image': 'https://images.unsplash.com/photo-1620712943543-2703222e3ae7?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=1200'},
    {'title': 'CyberSec Summit', 'date': 'Nov 18, 2025', 'desc': 'Learn about ethical hacking, network security, and cryptography from industry experts.', 'image': 'https://images.unsplash.com/photo-1550751827-4138d04d420d?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=1200'},
    {'title': 'Intro to Django', 'date': 'Dec 05, 2025', 'desc': 'Build and deploy your first web application with Python and Django. A beginner-friendly workshop.', 'image': 'https://images.unsplash.com/photo-1618423691278-c0705051827b?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=1200'},
    {'title': 'UI/UX Design Principles', 'date': 'Jan 10, 2026', 'desc': 'Master the fundamentals of user interface and user experience design with Figma.', 'image': 'https://images.unsplash.com/photo-1587440871875-191322ee64b0?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=1200'},
    {'title': 'Cloud Computing with AWS', 'date': 'Feb 22, 2026', 'desc': 'Explore cloud services and infrastructure with Amazon Web Services (AWS).', 'image': 'https://images.unsplash.com/photo-1563986768494-4dee2763ff3f?ixlib=rb-4.0.3&q=85&fm=jpg&crop=entropy&cs=srgb&w=1200'},
]

# --- TEAM DATA ---
team_data = {
    'advisor': {'name': 'Dr. Evelyn Reed', 'role': 'Faculty Advisor', 'img': 'https://i.pravatar.cc/300?u=advisor', 'linkedin': '#', 'github': '#'},
    'core': [
        {'name': 'Alex Johnson', 'role': 'Chairperson', 'img': 'https://i.pravatar.cc/300?u=chair', 'linkedin': '#', 'github': '#'},
        {'name': 'Maria Garcia', 'role': 'Vice Chairperson', 'img': 'https://i.pravatar.cc/300?u=vicechair', 'linkedin': '#', 'github': '#'},
        {'name': 'Chen Wei', 'role': 'Secretary', 'img': 'https://i.pravatar.cc/300?u=secretary', 'linkedin': '#', 'github': '#'},
        {'name': 'Samira Khan', 'role': 'Treasurer', 'img': 'https://i.pravatar.cc/300?u=treasurer', 'linkedin': '#', 'github': '#'},
    ],
    'tech': [
        {'name': 'Leo Martinez', 'role': 'Tech Head', 'img': 'https://i.pravatar.cc/300?u=techhead', 'linkedin': '#', 'github': '#'},
        {'name': 'Chloe Davis', 'role': 'Tech Member', 'img': 'https://i.pravatar.cc/300?u=tech1', 'linkedin': '#', 'github': '#'},
        {'name': 'Ben Carter', 'role': 'Tech Member', 'img': 'https://i.pravatar.cc/300?u=tech2', 'linkedin': '#', 'github': '#'},
    ],
    'design': [
        {'name': 'Priya Patel', 'role': 'Design Head', 'img': 'https://i.pravatar.cc/300?u=designhead', 'linkedin': '#', 'github': '#'},
        {'name': 'Oscar Kim', 'role': 'Design Member', 'img': 'https://i.pravatar.cc/300?u=design1', 'linkedin': '#', 'github': '#'},
    ],
    'membership': [
        {'name': 'Isabella Rossi', 'role': 'Membership Advisor', 'img': 'https://i.pravatar.cc/300?u=mem1', 'linkedin': '#', 'github': '#', 'phone': '919876543210'},
        {'name': 'Noah Brown', 'role': 'Membership Advisor', 'img': 'https://i.pravatar.cc/300?u=mem2', 'linkedin': '#', 'github': '#', 'phone': '919876543211'},
    ],
    'media': [
        {'name': 'Liam Wilson', 'role': 'Media Head', 'img': 'https://i.pravatar.cc/300?u=mediahead', 'linkedin': '#', 'github': '#'},
        {'name': 'Ava Miller', 'role': 'Media Member', 'img': 'https://i.pravatar.cc/300?u=media1', 'linkedin': '#', 'github': '#'},
    ],
    'content': [
        {'name': 'Sofia Taylor', 'role': 'Content Head', 'img': 'https://i.pravatar.cc/300?u=contenthead', 'linkedin': '#', 'github': '#'},
        {'name': 'James Moore', 'role': 'Content Writer', 'img': 'https://i.pravatar.cc/300?u=content1', 'linkedin': '#', 'github': '#'},
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
