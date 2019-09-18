import React, { Component } from 'react'
import { observer } from 'mobx-react'

import './RemoveDevice.css'

var RemoveDevice =  observer(class RemoveDevice extends Component {
    optionHandler = (option) => { this.props.uiState.managerSelection = option }
    render() {
        return (
            <div className="RemoveDevice">
                <div className='deviceList'>
                    {this.props.uiState.content.map((device) =>
                        <div className='device'>
                            <p><b>Nombre:</b> {device.name}</p>
                            <p><b>Variable:</b> {device.variable}</p>
                            <button
                                id="deviceButton"
                                onClick={() => { this.props.uiState.removeDevice(device) }}
                            >Eliminar dispositivo</button>
                        </div>
                    )
                    }
                </div>
                <button onClick={() => { this.optionHandler(null) } }>Regresar al menú anterior</button>
            </div>
            
        )
    }
})

export default RemoveDevice
