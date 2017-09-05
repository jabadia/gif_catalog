<template>
    <div class="row">
        <div class="col-12">
            <ul>
            <li v-for="pic in pics">{{pic.id}}.- {{pic.title}}</li>
            </ul>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                pics: [],
            };
        },
    };
</script>

<style lang="less" rel="stylesheet/less">
</style>
