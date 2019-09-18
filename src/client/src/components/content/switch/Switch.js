import React, { Component } from 'react'

import { observer } from 'mobx-react'

const Switch = observer (class Switch extends Component {
    componentWillUnmount() {
        this.props.uiState.setDevice(null)
    }
    render() {
        return (
            <div className="switch">
                <p><b>Nombre:</b> {this.props.uiState.device.name}</p>
                <p><b>Estado actual:</b> {this.props.uiState.device.variable} </p>
                <button onClick={() => 
                this.props.uiState.changeSwitchState(this.props.uiState.device.id)}
                >Cambiar estado</button>
                { this.props.uiState.device.registry === undefined ? 
                    <h1>Cargando</h1> 
                    :
                    <div className="registry">
                        <p><b>Últimos diez cambios: </b></p>
                    {this.props.uiState.device.registry.reverse().map((data) =>
                        <div>
                            <p>{data.time} {data.state}</p>
                        </div>
                    )}
                    </div>
                }
            </div>
        )
    }
})

export default Switch