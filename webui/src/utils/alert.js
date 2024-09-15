const handleAddToast = (alerts, setAlerts) => {
    setAlerts(alerts => [...alerts, {
        text: 'Please check your api key and try again',
        status: 'error'
    }]);
}

const handleRemoveToast = (index, alerts, setAlerts) => {
    setAlerts(alerts => alerts.filter((_, i) => i !== index));
}

export { handleAddToast, handleRemoveToast }
