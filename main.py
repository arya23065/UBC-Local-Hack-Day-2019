# Our Backend for the App!
# Built with Flask

# Import Flask
import flask

# Create the application
app = flask.Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


# path parameters
@app.route('/<name>')
def personal_hello(name):
    return "Hello " + name


# serving hello.html
@app.route('/fancy/<name>')
def some_page(name) :
    return flask.render_template('hello.html', name=name)


# serving find.html
@app.route('/find/<name>', methods=['GET'])
def some_page1(name) :
    return flask.render_template('find.html', name=name)


# process query
@app.route('/process_query', methods=['POST'])
def process_query():
    data = flask.request.form
    user_input = data['some_location']
    #print(user_input)

    index = 0
    answer = ['A', 'D', 'B', 'C', 'C', 'A']
    correct_answer = answer[index]


    if user_input == correct_answer:
        index += 1
        return flask.render_template('return_correct.html')
    elif user_input != correct_answer:
        index += 0
        return flask.render_template('return_incorrect.html')



    #return user_input

#     requestString = formRequest(location)
#     resopnces = makeGET(requestString) ['candidates']
#     return flask.render_template('find.html',resopnces=resopnces)

# def formRequest(localtion) : 




    

















if __name__ == '__main__':
    app.run(debug=True)
