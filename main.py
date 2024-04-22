import streamlit as st
from course import Course
from teacher import Teacher
from customer import Customer
from web_management import Web_Management

# Create an instance of Web_Management to manage teachers, courses, and customers
web_manager = Web_Management()

def main():
    st.title("Online Education Store")

    choice = st.radio("Are you a teacher or a customer?", ("Teacher", "Customer"))

    if choice == "Teacher":
        st.subheader("Teacher Portal")
        teacher_id = st.text_input("Enter Teacher ID:")
        teacher_name = st.text_input("Enter Teacher name:")

        teacher = Teacher(teacher_id, teacher_name)

        web_manager.add_teacher(teacher)

        if st.button("Create Course"):
            course_id = st.text_input("Enter Course ID:")
            course_title = st.text_input("Enter Course Title:")
            course_description = st.text_input("Enter Description:")
            course_price = st.number_input("Enter Course Price:", min_value=0.0)
            course_duration = st.number_input("Enter Course Duration (in hrs):", min_value=0.0)
            course_instructor = teacher_name

            course = Course(course_id, course_title, course_description, course_price, course_duration, course_instructor)

            teacher.create_course(course)
            web_manager.add_course(course)
            st.success("Course Added Successfully!!!!")

    elif choice == "Customer":
        st.subheader("Customer Portal")
        customer_id = st.text_input("Enter Username:")
        customer_name = st.text_input("Enter Customer Name:")

        customer = Customer(customer_id, customer_name)

        if st.button("Show All Courses"):
            available_courses = web_manager.display_available_courses()

            if not available_courses:
                st.write("No courses available.")
            else:
                st.write("Available Courses:")
                for course in available_courses:  #[java, python, c]
                    st.write(f"Course ID: {course.course_id}, Title: {course.title}, Price: ${course.price}, Duration: {course.duration} hrs, Instructor: {course.instructor}")

            selected_courses = st.multiselect("Select Courses to Add to Cart:", [course.title for course in available_courses]) #multiselect

            if st.button("Add to Cart"):
                for course_title in selected_courses:
                    course = next((i for i in available_courses if i.title == course_title), None) #__generator __next__
                    if course:
                        customer.add_to_cart(course)
                st.success("Courses added to cart!")

        if st.button("View Cart"):
            cart_courses = customer.view_cart()
            if cart_courses:
                st.write("Your Cart:")
                for course in cart_courses:
                    st.write(f"Course ID: {course.course_id}, Title: {course.title}, Price: ${course.price}, Duration: {course.duration} hrs")
                total_price = customer.calculate_total_price()
                st.write(f"Total Price: ${total_price}")
            else:
                st.write("Your cart is empty.")

if __name__ == "__main__":
    main()

