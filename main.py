import streamlit as st
from course import Course
from teacher import Teacher
from customer import Customer
from web_management import Web_Management



def main():
    st.title("Online Education Store")

    choice = st.radio("Are you teacher / customer?", ("Teacher", "Customer"))

    if choice == "Teacher":
        st.subheader("Teacher portal")
        teacher_id = st.text_input("Enter Teacher ID:")
        teacher_name = st.text_input("Enter Teacher name:")

        teacher = Teacher(teacher_id, teacher_name)

        Web_Management.add_teacher(teacher)
        if st.button("Create Course"):
            course_id = st.text_input("Enter Course ID: ")
            course_title = st.text_input("Enter Course Title:")
            course_description = st.text_input("Enter description: ")
            course_price = st.number_input("Enter Course Price: ")
            course_duration = st.number_input("Enter Course Duration(in hrs): ")
            course_instructor = st.text_input("Enter instructor name: ")

            course = Course(course_id, course_title, course_description, course_price, course_duration, course_instructor)

            Web_Management.add_course(course)
            st.success("Course Added Successfully!!!!!")


     elif choice == "Customer":
         st.subheader("Customer Portal")
         customer_id = st.text_input("Enter username: ")
         customer_name = st.text_input("Enter Customer name: ")

         customer = Customer(customer_id, customer_name)

     Web_Management.add_customer(customer)

         if st.button("Show All Course"):
             available_courses = web_management.display_available_courses()

             for course in available_courses:
                 st.write(f"Course ID: {course.course_id}, Title: {course.title}, Price: {course.price }, Description: {course.description}, Instructor: {course.instructor}, Duration: {Course.duration}")
                 if



