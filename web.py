import streamlit as st
import functions


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos = functions.get_todo()
    todos.append(new_todo)
    functions.write_todo(todos)


todo_list = functions.get_todo()

st.title("My To-Do App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=str(todo))
    if checkbox:
        todo_list.pop(index)
        functions.write_todo(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ",
              placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')
