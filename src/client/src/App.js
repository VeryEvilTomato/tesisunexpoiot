import React, { Component } from 'react'

import NavMenu from './components/nav/NavMenu'
import DeviceList from './components/content/DeviceList'
import Aside from './components/aside/Aside'
import axios from 'axios'

import './App.css';

export default class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			contentType: null,
			content: [],
			device: null,
			sidebar: null,
			userid: 1
		}
	}
	addDeviceHandler = () => {
		console.log("En progreso - Agregar dispositivo")
	}
	contentTypeHandler = (props) => {
		const {contentType, request} = props
		if(this.state.contentType !== contentType){
			this.setState({ contentType: contentType })
			axios.get('/api/user/' + this.state.userid + request).then(
				(response) => {
					this.setState({content: response.data.monitors})
				}
			)
		}
	}
	deviceSetHandler = (props) => {
		const {device} = props
		this.setState({device})
	}
	logoffHandler = () => {
		console.log(this.state.device)
    }
	render() {
		return (
			<main>
				<header>Universidad Nacional Experimental Politécnica “Antonio José de Sucre” Vicerrectorado Puerto Ordaz</header>
				<div className='container'>
					{/* Barra de navegación */}
					<div className='nav'>
						<img src="/images/unexpo_logo.png" alt="Logo UNEXPO" />
						<NavMenu
							contentTypeHandler={this.contentTypeHandler}
							logoffHandler={this.logoffHandler}
						/>
					</div>
					{/* Contenido central */}
					<div className='content'>
						{/* Selección/Agregar dispositivo */}
						<DeviceList 
							contentType={this.state.contentType}
							content={this.state.content}
							deviceSetCallback={this.deviceSetHandler}
						/>
						<div className='divisor'/>
						{/* Visualización del dispositivo */
							this.state.device === null ? "" :
							<div className='panel'>{this.state.device.name}</div>
						}
					</div>
					{/* Barra de información */}
					{ this.state.sidebar === null ? "" : <Aside/> }
				</div>
			</main>
		)
	}
}