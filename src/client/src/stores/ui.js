import { decorate, observable, action } from 'mobx'
import axios from 'axios'
import DeviceManager from '../components/content/device_manager/DeviceManager';

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
    emptyDate = false;
    status = null;
    // - Device data -
    managerSelection = null;
    options = null;
    content = null;
    device = null;
    dateSelected = new Date();
    dayData = dataReset

    setContent = (selection, selectionText) => {
        if (this.selection !== selection) {
            this.selection = selection;
            this.selectionText = selectionText;
            this.content = null;
            axios.get(`/api/user/${this.userId}/${selection}`)
            .then((response) => { this.content = response.data.content })
            .catch((error) => { alert(error.response.data.mensaje) })
        }
    }
    setDevicemanager = () => {
        this.selection = "manager";
        this.selectionText = "Gestor de Dispositivos"

        axios.get(`/api/user/${this.userId}/monitors`)
        .then((response) => { this.content = response.data.content })
        .catch((error) => { alert(error.response.data.mensaje) })

        axios.get(`/api/user/${this.userId}/options`)
        .then((response) => { this.options = response.data.content })
    }
    
    setDevice = (device) => {
        if(device !== this.device){
            this.device = device
            this.dayData = dataReset
            this.dateSelected = new Date();
        }
    }
    submitDevice = (deviceData) => {
        axios.post(`/api/user/${this.userId}/${deviceData.request}`, deviceData.jsonData)
        .then((response) => { 
            this.status = response.status
            if(this.status === 201) alert("Dispositivo correctamente agregado al sistema");
        })
        .catch((error) => { alert(error.response.data.mensaje) })
    }
    removeDevice = (device) => {
        console.log("Eliminado")
    }
    setDay = (date) => { 
        this.dateSelected = date;
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
    managerSelection: observable,
    option: observable,
    content: observable,
    device: observable,
    dateSelected: observable,
    dayData: observable,
    emptyDate: observable,
    status: observable,
    valor: observable,
    setContent: action,
    setDeviceManager: action,
    setDevice: action,
    setDay: action
})

export default uiState