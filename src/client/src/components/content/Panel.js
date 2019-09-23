import React, { Component } from 'react'
import { observer } from 'mobx-react'

import Monitor from './monitor/Monitor'
import Switch from './switch/Switch'

import './Panel.css'

const Panel = observer(class Panel extends Component {
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

export default Panel