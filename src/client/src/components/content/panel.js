import React, { Component } from 'react'
import { observer } from 'mobx-react'

import Monitor from './monitor/Monitor'
import Switch from './switch/Switch'

const panel = observer(class panel extends Component {
    renderSwitch(selection){
        switch (selection) {
            case "monitors":
                return <Monitor uiState={this.props.uiState} />
            case "switches":
                return <Switch uiState={this.props.uiState} />
            default:
                return ""
        }
    }
    render() {
        return (
            <div className='Panel'>
                {this.renderSwitch(this.props.uiState.selection)}
            </div>
        )
    }
})

export default panel