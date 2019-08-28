import { decorate, observable, action } from 'mobx'
import axios from 'axios'

class ui {
    userId = "1";
    selection = null;
    selectionText = null;
    content = null;

    setContent = (selection, selectionText) => {
        this.selection = selection;
        this.selectionText = selectionText
        axios.get(`/api/user/${this.userId}/${selection}`)
        .then((response) => { this.content = response.data.monitors });
    }
}

var uiState = window.uiDebug = new ui()

decorate(uiState, {
    userId: observable,
    selection: observable,
    selectionText: observable,
    content: observable,
    setContent: action
})

export default uiState