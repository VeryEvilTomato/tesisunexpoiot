import { decorate, observable, action } from 'mobx'
import axios from 'axios'

const dataReset = {
    labels: [null],
    datasets: [{
        label: "Lecturas",
        data: [{
            t: null,
            y: 1
        }],
        borderWidth: 1,
        backgroundColor: "#f1bc7f"
    }]
};

class ui {
    // - User data -
    userId = "1";
    // - UI data -
    selection = null;
    selectionText = null;
    wrongDate = false;
    emptyDate = false;
    // - Device data -
    content = null;
    device = null;
    dateSelected = new Date();
    dayData = dataReset

    setContent = (selection, selectionText) => {
        if (this.selection !== selection) {
            this.selection = selection;
            this.selectionText = selectionText
            axios.get(`/api/user/${this.userId}/${selection}`)
            .then((response) => { this.content = response.data.monitors });
        }
    }
    setDevice = (device) => {
        if(device !== this.device){
            this.device = device
            this.dayData = dataReset
        }
    }
    setDay = (date) => { 
        const dateNow = new Date();
        if(dateNow.getTime() < date.getTime()) { 
            this.wrongDate = true; 
            return 
        }
        this.dateSelected = date;
        this.wrongDate = false;
        this.dayDataRequest(date);
    }
    dayDataRequest = (date) => {
        let day = date.getDate().toString();
        let month = (date.getMonth() + 1).toString();
        let year = date.getFullYear().toString();
        let dateString = year + month + day;
        axios.get(`/api/user/${this.userId}/${this.selection}/${this.device.id}/data/date/${dateString}`)
        .then((response) => {
            if(response.data.data.length > 0) {
                this.processDayData(response.data.data);
                console.log("Procesado");
            }
            else {
                this.dayData = dataReset;
                this.emptyDate = true;
                console.log("Sin datos");
            }
        })
    }
    processDayData = (data) => {
        let newLabels = [], newData = []
        data.forEach((d) => {
            function check(n) {
                if(n < 10) { return "0" + n }
                else return n
            }
            let newDatum = {
                t: null,
                y: null
            };
            newLabels.push(`${check(d.time.hour)}:${check(d.time.hour)}`);
            newDatum.t = new Date(0, 0, 0, d.time.hour, d.time.min, 0, 0);
            newDatum.y = d.datum;
            newData.push(newDatum);
        })
        this.dayData.labels = newLabels;
        this.dayData.datasets[0].data = newData;
        this.emptyDate = false;
    }
}

var uiState = window.uiDebug = new ui()

// Decorador del store

decorate(uiState, {
    userId: observable,
    selection: observable,
    selectionText: observable,
    content: observable,
    device: observable,
    dateSelected: observable,
    wrongDate: observable,
    dayData: observable,
    emptyDate: observable,
    valor: observable,
    setContent: action,
    setDevice: action,
    setDay: action
})

export default uiState