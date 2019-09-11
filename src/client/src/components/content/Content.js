import React, { Component } from 'react'
import { observer } from 'mobx-react'

import Panel from './panel'
import DeviceList from './DeviceList'

import DeviceManager from './device_manager/DeviceManager'

import './Content.css'

const Content = observer(class Content extends Component {
    renderSwitch(selection) {
        switch(true) {
            case ("controls" === selection || "monitors" === selection):
                return <DeviceList uiState={this.props.uiState}/>
            case "manager" === selection:
                return <DeviceManager uiState={this.props.uiState}/>
        }
    }
    render() {
        return (
            <div className='Content'>
                <h2>{this.props.uiState.selectionText}</h2>
                {this.renderSwitch(this.props.uiState.selection)}
                {this.props.uiState.device == null ? "" :
                    <div>
                        <Panel uiState={this.props.uiState} />
                    </div>
                }
            </div>
        )
    }
})

export default Content