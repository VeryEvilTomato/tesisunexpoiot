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
    token = null;
    config = { headers:{ Authorization: ""} }
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
    isLoading = true;

    //Métodos del UI
    setContent = (selection, selectionText) => {
        this.isLoading = true;
        if (this.selection !== selection) {
            this.selection = selection;
            this.selectionText = selectionText;
            this.content = null;
            axios.get(`/api/user/${this.userId}/${selection}`, this.config)
            .then((response) => { this.content = response.data.content })
            .catch((error) => { 
                alert(error.response.data.mensaje)
                console.log(error.response.data)
            })
            .finally(() => { this.isLoading = false })
        }
    }
    setDevicemanager = () => {
        this.selection = "manager";
        this.selectionText = "Gestor de Dispositivos"
        this.updateContent("devices");
    }
    updateContent = (type) => {
        axios.get(`/api/user/${this.userId}/${type}`, this.config)
        .then((response) => { this.content = response.data.content })
        .catch((error) => { alert(error.response.data.mensaje) })

        axios.get(`/api/user/${this.userId}/options`, this.config)
        .then((response) => { this.options = response.data.content })
    }
    //Métodos del dispositivo
    setDevice = (device) => {
        if(device !== this.device){
            this.device = device
            this.dayData = dataReset
            this.dateSelected = new Date();
        }
    }
    submitDevice = (deviceData) => {
        axios.post(`/api/user/${this.userId}/${deviceData.request}`, deviceData.jsonData, this.config)
        .then((response) => { 
            this.status = response.status
            if(this.status === 201) {
                alert("Dispositivo correctamente agregado al sistema")
                this.updateContent("devices");
            };
        })
        .catch((error) => { alert(error.response.data.mensaje) })
        .finally(this.updateContent("devices"))
    }
    removeDevice = (device) => {
        const accept = window.confirm("¿Está seguro de querer borrar el dispositivo?")
        if(!accept) return
        axios.delete(`/api/user/${this.userId}/${device.type}/${device.id}`, this.config)
        .catch((error) => { alert(error.response.data.mensaje) })
        .finally(() => {
            this.updateContent("devices");
            alert("Dispositivo eliminado");
        })
    }
    //Monitores
    setDay = (date) => {
        this.dateSelected = date;
        this.dayDataRequest(date);
    }
    dayDataRequest = (date) => {
        let day = date.getDate().toString();
        let month = (date.getMonth() + 1).toString();
        let year = date.getFullYear().toString();
        let dateString = year + month + day;
        axios.get(`/api/user/${this.userId}/${this.selection}/${this.device.id}/data/date/${dateString}`, this.config)
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
            newLabels.push(`${check(d.time.hour)}:${check(d.time.min)}`);
            newDatum.t = new Date(0, 0, 0, d.time.hour, d.time.min, 0, 0);
            newDatum.y = d.datum;
            newData.push(newDatum);
        })
        this.dayData.labels = newLabels;
        this.dayData.datasets[0].data = newData;
        this.emptyDate = false;
    }
    //Switches
    changeSwitchState = (switchID) => {
        this.isLoading = true;
        axios.put(`/api/user/${this.userId}/switches/${switchID}`, null, this.config)
        .then((response) => { this.updateContent("switches") })
        .catch((error) => { alert(error.response.data.mensaje) })
        .finally(() => {
            axios.get(`/api/user/${this.userId}/switches/${switchID}`, this.config)
            .then((response) => {
                this.device = response.data.device;
                this.isLoading = false;
            })
        })
    }
    //Autenticación
    userRegister = (username, password) => {
        axios.post('/api/user/register', {
            user: username,
            password: password
        }).then((response) => {
            alert("Usuario registrado")
        }).catch((error) => {
            alert("Error")
            console.log(error.response)
        })
    }
    userLogin = (username, password) => {
        axios.post(`/auth`, {
            username: username,
            password: password
        }).then((response) => {
            const token = response.data.access_token;
            this.token = token;
            this.config.headers["Authorization"] = `JWT ${this.token}` 
            axios.post(`/api/user/id`,{
                user: username,
                password: password
            })
            .then((response) => {
                this.userId = response.data.id
            })
            .catch((error) => {
                console.log(error.response)
                alert("Error")
            })
        }).catch((error) => {
            alert("Credenciales inválidos")
        })
    }
}

var uiState = window.uiDebug = new ui()

// Decorador del store

decorate(uiState, {
    userId: observable,
    token: observable,
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
    isLoading: observable,
    setContent: action,
    updateData: action,
    setDeviceManager: action,
    setDevice: action,
    setDay: action
})

export default uiState