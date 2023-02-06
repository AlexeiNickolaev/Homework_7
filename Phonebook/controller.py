import view
import process
import log

def button_click():
    rezhim = view.inp_mod()
    if rezhim.lower() == '1':
        sern = view.inp_import()
        res_search = process.search(sern)
        if isinstance(res_search, str):
            view.view_import_no()
        else:
            view.view_import(res_search)
        log.log_imp(sern)
    elif rezhim.lower() == '2':
        result = view.inp_export()
        process.export(result)
        log.log_exp(result)
