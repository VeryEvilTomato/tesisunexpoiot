import React, { Component } from 'react'
import { observer } from 'mobx-react'

import Panel from './panel'

import './Content.css'

const Content = observer(class Content extends Component {
    render() {
        return (
            <div className='Content'>
                <h2>{ this.props.uiState.selectionText }</h2>
                <div className='deviceList'>
                    { this.props.uiState.content.map((device) =>
                        <div className='device'>
                            <p><b>Nombre:</b> {device.name}</p>
                            <p><b>Variable:</b> {device.variable}</p>
                            <button
                                id="deviceButton"
                                onClick={() => {this.props.uiState.setDevice(device) }}
                            >Seleccionar dispositivo</button>
                        </div>
                    )
                    }
                </div>
                { this.props.uiState.device == null ? "" :
                    <div>
                        <div id="division"></div>
                        <Panel uiState={this.props.uiState}/>
                    </div>
                }
            </div>
        )
    }
})

export default Content