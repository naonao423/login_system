from chalice import Chalice,NotFoundError,BadRequestError
from chalicelib import database

app = Chalice(app_name='Login_system')

@app.route('/login',cors=True,methods=["POST"])
def check_id_pass():
    id_pass_dic = app.current_request.json_body
    print(id_pass_dic)
    result = database.check_id_pass(id_pass_dic)
    return result
            
@app.route('/logout',cors=True,methods=["POST"])
def delete_session_id():
    id_pass_dic = app.current_request.json_body
    print(id_pass_dic)
    return database.delete_session_id(id_pass_dic)

@app.route('/check',methods=["POST"],cors=True)
def check_session_id():
    session_id_dic = app.current_request.json_body
    print(session_id_dic)
    result = database.check_session_id(session_id_dic)
    return result
