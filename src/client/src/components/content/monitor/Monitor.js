import React, { Component } from 'react'
import { observer } from 'mobx-react'

import DatePicker from 'react-datepicker'
import { registerLocale } from  "react-datepicker";
import es from 'date-fns/locale/es';
import { Line } from 'react-chartjs-2';

import "./Monitor.css"
import "./LineChart.css"
import "react-datepicker/dist/react-datepicker.css";
import { addDays } from 'date-fns';

registerLocale('es', es)

const Monitor = observer( class Monitor extends Component {
	constructor(props){
		super(props);
		this.chartReference = {}
		this.hideChart = false;
		this.state = {
			mostrar: false,
			data: {
				labels: [null],
				datasets: [{
					label: "Lecturas",
					data: [{
						t: null,
						y: 1
					}],
					borderWidth: 1,
					backgroundColor: "#f1bc7f",
					pointRadius: 5
				}]
			},
			options: {
				responsive: true,
				maintainAspectRatio: 1,
				showLine: false,
				elements: {
					line: {
						tension: 0
					},
					// scales: {
					// 	xAxes: [{
					// 		type: 'time',
					// 		distribution: 'linear',
					// 		time: {
					// 			parser: 'HH:mm',
					// 			tooltipFormat: 'HH:mm',
					// 			unit: 'minute',
					// 			stepSize: 10,
					// 			displayFormats: {
					// 			  'minute': 'HH:mm',
					// 			  'hour': 'HH:mm'
					// 			}
					// 		  }
					// 	}]
					// }
				},
				animation: { duration: 0 },
				hover: { animationDuration: 0 },
				responsiveAnimationDuration: 0 
			}
		}
	}
	componentDidMount(){
		const datePickers = document.getElementsByClassName("react-datepicker__input-container");
    	Array.from(datePickers).forEach((el => el.childNodes[0].setAttribute("readOnly", true)))
		this.chartUpdate = setInterval(() => {
			this.setState({data: this.props.uiState.dayData});
			console.log("Update")
		}, 1000)
	}
	componentWillUnmount(){
		this.chartReference.chartInstance.destroy();
		clearInterval(this.chartUpdate);
		this.props.uiState.setDevice(null)
	}
	dateHandler = (date) => { this.props.uiState.setDay(date) }
    render() {
        return (
            <div>
				<div id="division"></div>
				<h2>{ this.props.uiState.device.name }</h2>
                <p>El monitor visualiza todos los datos recaudados por el dispositivo durante <i>un día completo</i>, para seleccionar un día, por favor <b>clickear</b> la fecha en el recuadro.</p>
                <div className="datepicker">
                    <DatePicker
						placeholderText="Clickear para seleccionar una fecha"
                        selected={this.props.uiState.dateSelected}
                        onChange={this.dateHandler}
						locale="es"
						maxDate={addDays(new Date(),0)}
                    />
					{this.props.uiState.emptyDate ?
						<p>No existen datos registrados para la fecha suministrada</p>
						:
						<button
							onClick={ () => {
								this.dateHandler(this.props.uiState.dateSelected)
							}}
						>Refrescar datos</button>
					}
                </div>
                <br/>
				<Line
					ref={(reference) => this.chartReference = reference}
					data={this.state.data}
					options={this.state.options}
				/>
            </div>
        )
    }
})

export default Monitor