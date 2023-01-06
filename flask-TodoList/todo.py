import flask, os, sqlite3 
from flask import render_template, request, send_from_directory 
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)

def fetchlist():
    db = sqlite3.connect('todo.db')
    db.row_factory = sqlite3.Row
    cursor = db.execute("SELECT todo.ID as id,\
                        category.Name as categoryname, \
                        todo.Description as description, \
                        todo.Image as imageURL, \
                        todo.Status as status, \
                        todo.AddOn as addon \
                        FROM todo INNER JOIN category on todo.Category = category.ID") 
    res = cursor.fetchall()
    db.close()
    return res

def fetchcat():
    db = sqlite3.connect('todo.db')
    db.row_factory = sqlite3.Row
    cursor = db.execute("SELECT ID as id, Name as name FROM Category")
    res = cursor.fetchall()
    db.close() 
    return res

def fetchitem(itemID):
    db = sqlite3.connect('todo.db')
    db.row_factory = sqlite3.Row
    cursor = db.execute("SELECT todo.Category as category, \
                        category.Name as categoryname, \
                        todo.Description as description, \
                        todo.Image as imageURL, \
                        todo.Status as status, \
                        todo.AddOn as addon \
                        FROM todo INNER JOIN category on todo.Category = category.ID\
						WHERE todo.id = ?", (itemID))
    res = cursor.fetchall()
    db.close()
    return res 
    
@app.route('/')
def index():
    todolist = fetchlist()
    return render_template('todo.html', todolist=fetchlist())

def deleteitem(itemID):
    try: 
        db = sqlite3.connect('todo.db')
        db.execute('DELETE FROM todo \
                    WHERE id = ?', (itemID)) 
        db.commit()
        db.close()
        return True
    except:
        return False 

@app.route('/delete', methods=['GET', 'POST']) 
def delete():
    itemID = request.args.get('itemID')
    if request.method == 'GET':
        print('itemID1: ', itemID) 
        return render_template('deletetodo.html', itemID = itemID, categories = fetchcat(), items = fetchitem(itemID))
    else:
        success = deleteitem(itemID)
        if success:
            return render_template('editresult.html', resulttext = 'Success!', itemID = itemID)
        else:
            return render_template('editresult.html', resulttext = 'Error', itemID = itemID) 
        
def edititem(itemID, data, photo):  
    try:
        if photo:
            filename = secure_filename(photo.filename)
            path = os.path.join('uploads', filename)
            photo.save(path)
        else:
            filename = None
        print('filename: ', filename) 
        categoryID = data['categoryID'] 
        description = data['description']
        status = data['status']
        print(status) 
        db = sqlite3.connect('todo.db')
        if categoryID != "":
            db.execute(" UPDATE todo \
                        SET Category =? WHERE todo.id = ?" , (categoryID, itemID))
        if description != "":
            db.execute(" UPDATE todo \
                        SET Description = ? WHERE todo.id = ?", (description, itemID))
        if status != "":
            db.execute("UPDATE todo \
                        SET Status = ?  WHERE todo.id = ?", (status, itemID))
        if filename != "":
            db.execute("UPDATE todo \
                        SET Image = ? WHERE todo.id = ?", (filename, itemID)) 
        db.commit()
        db.close() 
        return True
    except:
        return False 

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    itemID = request.args.get('itemID')
    if request.method == 'GET':
        print('itemID1: ', itemID) 
        return render_template('edittodo.html', itemID=itemID, categories = fetchcat(), item = fetchitem(itemID))
    else:
        if request.files and 'photo' in request.files:
            photo = request.files['photo']
        else:
            photo = None
        print(photo)
        print('itemID2: ', itemID) 
        success = edititem(itemID, request.form, photo) 
        if success:
            return render_template('editresult.html', resulttext = 'Success!', itemID = itemID)
        else:
            return render_template('editresult.html', resulttext = 'Error', itemID = itemID) 

@app.route('/photos/<filename>')
def getfile(filename):
    return send_from_directory('uploads', filename)

def additem(data, photo):
    print(data)
    try:
        if photo:
            filename = secure_filename(photo.filename)
            path = os.path.join('uploads', filename)
            photo.save(path)
        else:
            filename = None 

        categoryID = data['categoryID']
        description = data['description']
        db = sqlite3.connect('todo.db')
        db.execute("INSERT INTO todo(Category, Description, Image, Status, AddOn) \
                    VALUES (?, ?, ?, 'Pending', datetime('now', 'localtime'))", \
                   (categoryID, description, filename,))
        db.commit()
        db.close() 
        return True
    except:
        return False 

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('addtodo.html', categories = fetchcat())
    else:
        if request.files and 'photo' in request.files:
            photo = request.files['photo']
        else:
            photo = None
        success = additem(request.form, photo)
        if success:
            return render_template('addresult.html', resulttext = "Success!")
        else:
            return render_template('addresult.html', resulttext = "Error") 

if __name__ == '__main__':
    app.run() 
