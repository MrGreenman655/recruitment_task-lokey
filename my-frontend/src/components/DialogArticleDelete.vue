<template>
  <q-dialog v-model="modalData.isDialogOpen">
    <q-card style="width: 500px">
      <q-form class="q-gutter-md q-pa-md">
        <q-card-section class="row items-center">
          <q-avatar icon="delete" color="negative" text-color="white"/>
          <span class="q-ml-sm">Are you sure you want to remove this article?</span>
        </q-card-section>
        <q-card-section>
          <q-input v-model="modalData.article_id" readonly></q-input>
          <q-input v-model="modalData.title" readonly></q-input>
          <q-input v-model="modalData.release_date" readonly></q-input>
          <q-input v-model="modalData.content" readonly></q-input>
        </q-card-section>
        <q-card-actions align="right">
          <q-btn flat label="Cancel" color="grey" v-close-popup />
          <q-btn @click="deleteArticle" flat label="Delete" color="negative"/>
        </q-card-actions>
      </q-form>
    </q-card>

  </q-dialog>
</template>

<script setup lang="ts">

import {reactive} from "vue";
import {api} from "boot/axios";
import {articleDetailEndpoint} from "src/api";
import {Notify} from "quasar";

const modalData: IModalData = reactive({
  article_id: '',
  title: '',
  release_date: '',
  content: '',
  isDialogOpen: false,
})

defineExpose({modalData})
const emits = defineEmits(['deleteDone'])
export interface IModalData {
  article_id: string,
  title: string,
  release_date: string,
  content: string,
  isDialogOpen: boolean,
}

const deleteArticle = async () => {
  try{
    await api.delete(articleDetailEndpoint.replace('{article_id}', modalData.article_id))
    Notify.create({message:'Article has been deleted',color:"green"})
    modalData.isDialogOpen = false
    emits('deleteDone')
  }
  catch(e) {
    Notify.create({message:'Failed to delete article',color:"negative"})
  }
}
</script>

<style scoped>

</style>
