### Streamlit with Python

### Hosted by Ibrahim (IET, IEEE) on July 2022

**GUI Libraries in Python**
1. tkinter
2. Qt from C++
3. Panel (Drag and Drop)
4. Dash (with HTML)
5. Streamlit (easiest)
6. Plotly Express

- python 3.9 only support streamlit steadily

**Good python programming practice**
```
def main():
    pass

if __name__ = "__main__":
    main()    
```

**Dive in into Streamlit**

1. ``st.write("# Heading")``
    - in terminals ``run: streamlit run ./filename.py``
    - ``write`` can takes in many data format like markdown, images, html 
    - ``""""""`` means multiline comments
    - display different for a dictionary
    - can read dataframe, even ``df.describe()``
    - passing in figures
2. ``st.image("img.png")``
3. ``st.latex("\frac{}{}")``
3. ``st.line_chart(dictionary)``
4. ``st.bar_chart()``
 
**Dealing with Input Data**
1. ``numvar = st.number_input("Enter a Number", value=dafault number, min_value = 0, max_value = 1, step = 1)``
2. ``selection = st.selection("Text", options = ["A", "B", "C"]``)
    ```
    if selection == "A":
        print("A)
    ```
3. ``file = st.file_uploader("Upload a file", type = ["csv"])``
    ```
    if file is not None:
        df = pd.read_csv(file)
        st.write(df)
    ```

**Section Storage**
- ``st.session`` 

**Layout**
- Sidebar
    - ``power = st.sidebar.radio("Label", [1,2,3])``
    - ``power = st.sidebar.selectbox("Label", [1,2,3])``
- Columns
    - ``col1, col2 = st.columns(2)``
    ```
    with col1:
        st.write("# Write something")
    
    # Alternatively

    col2.write("# Write another thing")
    ``` 
- Tabs
    ```
    speaker_tab, speaker_event = st.tabs(["Speakers", "Events"])

    with speaker_tab:
        st.tile("Speaker")
        st.subheader("Speaker")
        st.write("Speaker")
    
    with speaker_event:
        st.title("Event")
        st.subheader("Event")
        st.write("Event")
    ```

**Calling Functions with Buttons**
- ```
    def fake_function():
        sleep(7)
        return 10

    btn = st.button("Start")

    if btn:
        with st.spinner("Display me when functions running")
            x = fake_function
            st.success(f"Done, x is {x}")
    ```

**Making a form** to prevent instantaneous calculation especially on the user input
-   ```
    with st.form(key = "Experiment"):
        x = st.number_input("X value")
        y = st.number_input("Y value")

        submit = st.form_submit_button("Calculate")

        if submit:
            st.write(runfunction)
    ```

- decorator: ``@st.cache`` saves the variable into cache memory, so that it checks if there is a need to recalculate before running the buttons, it put in one line above the function to be cached

**Creating Multiple Pages Web Applications**
1. Method 1: By creating a folder named pages, and placing different py file inside the directory, folder same as the parent py file, it will create a sidebar for navigation by default
2. Using the streamlit way
-   ```
    from foldername import pyfile
    ```
- use tab for it to switch the tabs

**How to mimic real time data in graph using functions**

**Cloud upload using github account by naming python file as streamlit_app.py**.

**Alternative Libraries for Web Applications in Python**
- https://panel.holoviz.org/gallery/demos/VTKInteractive.html#demos-gallery-vtkinteractive

- https://dash.gallery/Portal/

- https://www.qt.io/ : check out PyQt
