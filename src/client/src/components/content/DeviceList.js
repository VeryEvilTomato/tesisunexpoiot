import React, { Component } from 'react'
import { observer } from 'mobx-react'

var DeviceList =  observer(class DeviceList extends Component {
    render() {
        return (
            <div className='deviceList'>
                {this.props.uiState.content === null ?
                    <h1>Cargando</h1>
                    :
                    this.props.uiState.content.map((device) =>
                        <div className='device'>
                            <p><b>Nombre:</b> {device.name}</p>
                            <p><b>Variable:</b> {device.variable}</p>
                            <button
                                id="deviceButton"
                                onClick={() => { this.props.uiState.setDevice(device) }}
                            >Seleccionar dispositivo</button>
                        </div>
                    )
                }
            </div>
        )
    }
})

export default DeviceList
