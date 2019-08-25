import { decorate, observable, action } from 'mobx'

export default class uiStore {
    contentType;

    setContentType(contentType) {
        this.contentType = contentType;
    }
}

decorate(uiStore,{
    contentType: observable,
    setContentType: action
})