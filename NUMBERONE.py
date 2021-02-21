from flask import Flask, request
from flask import url_for

app = Flask(__name__)


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align=center>Анкета претендента</h1>
                            <h2 align=center>на участие в секретной миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="emailHelp" placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                 <br>   
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее неоконченное</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
   <br>                                     
                                    <label for="classSelect">Какие у Вас есть профессии?</label>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Инженер-исследователь</label>
<br>
                                        <input type="checkbox" class="form-check-input1" id="acceptRules1" name="accept1">
                                        <label class="form-check-label" for="acceptRules1">Инженер-строитель</label>
<br>
                                        <input type="checkbox" class="form-check-input2" id="acceptRules2" name="accept2">
                                        <label class="form-check-label" for="acceptRules2">Пилот</label>
<br>
                                        <input type="checkbox" class="form-check-input3" id="acceptRules3" name="accept3">
                                        <label class="form-check-label" for="acceptRules3">Метеоролог</label>
<br>
                                        <input type="checkbox" class="form-check-input4" id="acceptRules4" name="accept4">
                                        <label class="form-check-label" for="acceptRules4">Инженер по жизнеобеспечению</label>
<br>
                                        <input type="checkbox" class="form-check-input5" id="acceptRules5" name="accept5">
                                        <label class="form-check-label" for="acceptRules5">Инженер по радиационной защите</label>
<br>
                                        <input type="checkbox" class="form-check-input7" id="acceptRules7" name="accept7">
                                        <label class="form-check-label" for="acceptRules7">Врач</label>
                                        <br>
                                        <input type="checkbox" class="form-check-input8" id="acceptRules8" name="accept8">
                                        <label class="form-check-label" for="acceptRules8">Экзобиолог</label>
                                    </div>
<br>


                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                  <br>  
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>

<br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label><br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group2 form-check">
                                        <input type="checkbox" class="form-check-input9" id="acceptRules" name="accept">
                                        <label class="form-check-label9" for="acceptRules">Готов(а) остаться на Марсе</label>
                                    </div>
<br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')