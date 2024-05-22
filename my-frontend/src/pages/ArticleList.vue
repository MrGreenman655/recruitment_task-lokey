<template>
  <q-page class="row items-center justify-evenly">
    <q-card>
      <q-card-actions align="right">
        <q-btn @click="openArticleCreateModal" label="Create Article" color="primary"/>
      </q-card-actions>
      <q-card-section>
        <q-table
          title="Articles"
          :rows="rows"
          :columns="columns"
        >
          <template v-slot:body-cell-actions="props">
            <q-td :props="props" class="q-gutter-xs">
              <q-btn @click="openArticleEditModal(props.row)" size="xs" color="primary" round icon="edit"></q-btn>
              <q-btn @click="openArticleDeleteModal(props.row)" size="xs" color="negative" round icon="delete"></q-btn>
            </q-td>
          </template>
        </q-table>
      </q-card-section>

    </q-card>
    <DialogArticleDelete ref="articleDeleteModal" @delete-done="fetchArticles"/>
    <DialogArticleCreate ref="articleCreateModal" @create-done="fetchArticles"/>
    <DialogArticleEdit ref="articleEditModal" @edit-done="fetchArticles"/>
  </q-page>

</template>

<script setup lang="ts">
import {defineComponent, onMounted, ref} from 'vue';
import {api} from "boot/axios";
import {articlesEndpoint} from "src/api";
import {Notify} from "quasar";
import DialogArticleDelete from "components/DialogArticleDelete.vue";
import DialogArticleCreate from "components/DialogArticleCreate.vue";
import DialogArticleEdit from "components/DialogArticleEdit.vue";


defineComponent({
  name: 'ArticleList'
});

const columns = [
  {field: row => row.article_id, name: 'article_id', align: 'center', label: 'ID'},
  {field: row => row.title, name: 'title', align: 'center', label: 'Title'},
  {
    field: row => `${row.content.split(/\s+/).slice(0, 5).join(" ")}...`,
    name: 'content',
    align: 'center',
    label: 'Content'
  },
  {field: row => row.release_date, name: 'release_date', align: 'center', label: 'Release Date'},
  {field: '', name: 'actions', align: 'center', label: 'Actions'},
]
let rows = ref<IArticleRow[]>([])

onMounted(async () => {
  await fetchArticles()
})

const fetchArticles = async () => {
  try {
    const response = await api.get(articlesEndpoint)
    rows.value = response.data
  } catch {
    Notify.create({
        message: 'Failed to fetch data',
        color: 'negative'
      }
    )
  }
}
const articleDeleteModal = ref<InstanceType<typeof DialogArticleDelete>>()
const openArticleDeleteModal = (rows: IArticleRow) => {
  articleDeleteModal.value.modalData.article_id = rows.article_id
  articleDeleteModal.value.modalData.title = rows.title
  articleDeleteModal.value.modalData.content = rows.content
  articleDeleteModal.value.modalData.release_date = rows.release_date
  articleDeleteModal.value.modalData.isDialogOpen = true
}

const articleCreateModal = ref<InstanceType<typeof DialogArticleCreate>>()
const openArticleCreateModal = () => {
  articleCreateModal.value.modalData.title = ''
  articleCreateModal.value.modalData.content = ''
  articleCreateModal.value.modalData.release_date = ''
  articleCreateModal.value.modalData.isDialogOpen = true
}
const articleEditModal = ref<InstanceType<typeof DialogArticleEdit>>()
const openArticleEditModal = (rows: IArticleRow) => {
  articleEditModal.value.modalData.article_id = rows.article_id
  articleEditModal.value.modalData.title = rows.title
  articleEditModal.value.modalData.content = rows.content
  articleEditModal.value.modalData.release_date = rows.release_date
  articleEditModal.value.modalData.isDialogOpen = true
}

interface IArticleRow {
  article_id: string,
  title: string,
  content: string,
  release_date: string,
}
</script>
