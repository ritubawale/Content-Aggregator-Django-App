import requests
from bs4 import BeautifulSoup
from courses.models import Course


def scrape_courses():
    # Example scraping from a platform like Coursera
    url = "https://www.coursera.org/courses"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    courses = soup.find_all('div', class_='course-card')
    for course in courses:
        title = course.find('h2').text
        course_url = course.find('a')['href']
        description = course.find('p').text
        price = "Free"  # Adjust based on actual data
        rating = float(course.find('span', class_='rating').text)

        Course.objects.update_or_create(
            platform="Coursera",
            title=title,
            defaults={
                'url': course_url,
                'description': description,
                'price': price,
                'rating': rating,
            }
        )


if __name__ == "__main__":
    scrape_courses()
