import webbrowser

from flask import Flask, render_template, json, jsonify, request, send_from_directory
from kantahaut import LaatuSearch
from PDF_eco_report import reportPDF

app = Flask(__name__)
kan = LaatuSearch()


@app.route('/ecodb')
def eco_table():
    return '<h1>ECO-DB Web App</h1>'
    # render_template('base.html')


@app.route('/print')
def print_eco_report():
    eco_name = request.args.get('eco_name_send'.strip())
    print(eco_name)
    filedetails = reportPDF(str(eco_name))
    return send_from_directory(directory=filedetails[0],
                               filename=filedetails[1].strip(),
                               mimetype='application/pdf', cache_timeout=0)


@app.route('/ecobysuppliers')
def suppliers_table():
    return render_template('ecoBysuppliers.html')


@app.route('/description', methods=['GET', 'POST'])
def data():
    all_ecos_table = kan.table_all_ecos()
    all_ecos_table_dict = list(dict.fromkeys(all_ecos_table))
    active_ecos_table = []
    for x in all_ecos_table_dict:
        if x[8] == '':
            active_ecos_table.append(x)
            active_ecos_table.reverse()
    # print(json.dumps(active_ecos_table))
    return jsonify({'data': active_ecos_table})


@app.route('/active')
def active_ecos():   
    return render_template('activeEcos.html')


@app.route('/all')
def all_ecos():   
    return render_template('allEcosTable.html')


@app.route('/all_ecos')
def all_ecos_table():
    all_ecos_table = kan.table_all_ecos()
    all_ecos_table_dict = list(dict.fromkeys(all_ecos_table))
    all_ecos_table_dict.reverse()
    return jsonify({'data': all_ecos_table_dict})


@app.route('/active_ecos')
def active_ecos_table():
    all_ecos_table = kan.table_all_ecos()
    all_ecos_table_dict = list(dict.fromkeys(all_ecos_table))
    active_ecos_table = []
    for x in all_ecos_table_dict:
        if x[8] == '':
            active_ecos_table.append(x)
            active_ecos_table.reverse()
    return jsonify({'data': active_ecos_table})


@app.route('/all_items')
def all_items_table():
    items = kan.table_items()
    all_items_table_dict = list(dict.fromkeys(items))
    # all_items_table_dict.reverse()
    return jsonify({'data': all_items_table_dict})


@app.route('/active_items')
def active_items_table():
    all_ecos_table = kan.table_all_ecos()
    all_ecos_table_dict = list(dict.fromkeys(all_ecos_table))
    active_ecos_table = []
    for x in all_ecos_table_dict:
        if x[8] == '':
            active_ecos_table.append(x)
            active_ecos_table.reverse()

    item_table = kan.table_items()
    eco_name_ac = list(dict.fromkeys([x[0] for x in active_ecos_table]))
    eco_items_active = []
    for x in item_table:
        if x[0] in eco_name_ac:
            eco_items_active.append(x)
            eco_items_active.reverse()
    return jsonify({'data': eco_items_active})


@app.route('/bysuppliers')
def ecos_by_suppliers():
    supplier_table = kan.ecos_by_suppliers()
    return jsonify({'data': supplier_table})


@app.route('/bysuppliersanditems')
def supplierItems():
    supplier_items_table = kan.table_suppliers_n_items()
    return jsonify({'data': supplier_items_table})


@app.route('/supplieritems')
def suppliers_n_items():
    return render_template('suppliersAnditems.html')


@app.route('/items')
def items():
    items = kan.table_items()
    return jsonify({'data': items})


@app.route('/byitems')
def items_only():
    return render_template('items.html')


@app.route('/update_date_imp', methods=['GET', 'POST'])
def update_date_imp():
    date_imp = request.form.get("value")
    eco_name = request.form.get("id")

    update = """UPDATE [dbo].[ECO_Uudet_Ecot] SET
                    [ECO_Impl_in_production] = '""" + str(date_imp) + """'
    		        WHERE ECO_Name = '""" + str(eco_name) + """'"""

    kan.cursor.execute(update)
    # print(date_imp)
    # print(eco_name)
    return date_imp


@app.route('/update_date_ver', methods=['GET', 'POST'])
def update_date_ver():
    date_ver = request.form.get("value")
    eco_name = request.form.get("id")

    update = """UPDATE [dbo].[ECO_Uudet_Ecot] SET
                    [ECO_Impl_verified_date] = '""" + str(date_ver) + """'
    		        WHERE ECO_Name = '""" + str(eco_name) + """'"""

    kan.cursor.execute(update)
    # print(date_ver)
    # print(eco_name)
    return date_ver


@app.route('/update_comment', methods=['GET', 'POST'])
def update_comment():
    # date = request.get_json('sentText')
    comment = request.form.get("value")
    # j = request.args.get('impl_date')
    eco_name = request.form.get("id")

    update_query = """UPDATE [dbo].[ECO_Uudet_Ecot] SET
                    [Tracking_comment] = '""" + str(comment) + """'
    		        WHERE ECO_Name = '""" + str(eco_name) + """'"""
    kan.cursor.execute(update_query)
    return comment


if __name__ == '__main__':
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://127.0.0.1:5000/active",
                                                                                          new=0)
    app.run()
