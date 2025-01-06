function updateCounter(elementId) {
    let _$counterElement = document.getElementById(elementId);
    let _$count = _$counterElement.innerHTML;
    _$count = Number(_$count) + 1;
    _$counterElement.innerHTML = _$count;
}