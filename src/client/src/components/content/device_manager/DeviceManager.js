import React, { Component } from 'react'

import  { observer } from 'mobx-react'

import AddDevice from './AddDevice'
import RemoveDevice from './RemoveDevice'

const DeviceManager = observer (class DeviceManager extends Component {
    renderSwitch(option) {
        switch(option) {
            case "add":
                return <AddDevice uiState={this.props.uiState}/>
            case "delete":
                return <RemoveDevice uiState={this.props.uiState}/>
            default: return ""
        }
    }
    componentDidMount() { this.props.uiState.managerSelection = null }
    optionHandler = (option) => { this.props.uiState.managerSelection = option }
    render() {
        return (
            <div>
                {this.props.uiState.managerSelection !== null ? "" :
                    <div className="devicemanager">
                        <button onClick={() => { this.optionHandler("add") } }>Agregar dispositivo</button>
                        <button onClick={() => { this.optionHandler("delete")} }>Eliminar dispositivo</button>
                    </div>
                }
                {this.renderSwitch(this.props.uiState.managerSelection)}
            </div>
        )
    }
})

export default DeviceManager