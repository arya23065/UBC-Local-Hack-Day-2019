# Our Backend for the App!
# Built with Flask

# Import Flask
import flask

# Create the application
app = flask.Flask(__name__)

index = 0
answer = ['Rio Grande', 'B', 'C', 'D', 'E', 'F']

@app.route('/')
def some_page2():
    return flask.render_template('quiz2.html')


# path parameters
# @app.route('/<name>')
# def personal_hello(name):
#     return "Hello " + name


# # serving hello.html
# @app.route('/fancy/<name>')
# def some_page(name) :
#     return flask.render_template('starterpage.html', name=name)
#
#
# # serving find.html
# @app.route('/quiz', methods=['GET'])
# def some_page1():
#     return flask.render_template('quiz.html')


# process query
@app.route('/process_query', methods=['GET', 'POST'])
def process_query():
    data = flask.request.form.get('options')
    print(data)
    user_input = str(data)

    global index
    global answer
    
    correct_answer = answer[index]

    if user_input == correct_answer:
        index += 1
        return flask.render_template('return_correct.html')
    elif user_input != correct_answer:
        index += 0
        return flask.render_template('return_incorrect.html')


@app.route('/correct_page', methods=['GET'])
def correct_page():
    return flask.render_template('return_correct.html')

@app.route('/incorrect_page', methods=['GET'])
def incorrect_page():    
        return flask.render_template('return_incorrect.html')






    #return user_input

#     requestString = formRequest(location)
#     resopnces = makeGET(requestString) ['candidates']
#     return flask.render_template('find.html',resopnces=resopnces)

# def formRequest(localtion) : 



if __name__ == '__main__':
    app.run(debug=True)
