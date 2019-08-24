import React, { Component } from 'react'
import UtilButton from '../helpers/UtilButton'
import './DeviceList.css'

export default class DeviceList extends Component {
    render() {
        return (
            <div className='deviceList'>
                <h3>{this.props.contentType}</h3>
                {
                    this.props.content.map(device => {
                        return <div className='deviceContainer'>
                            <p><b>Nombre: </b> {device.name}</p>
                            <p><b>Variable: </b> {device.variable}</p>
                            <UtilButton
                                functionCallback = {this.props.deviceSetCallback}
                                device = {device}
                                contentType = 'Seleccionar dispositivo'
                            />
                        </div>
                        
                    })
                }
            </div>
        )
    }
}